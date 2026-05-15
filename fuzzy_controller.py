import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# ==========================================================
# Giriş Değişkenleri
# ==========================================================

sicaklik = ctrl.Antecedent(np.arange(0, 41, 1), 'sicaklik')
nem = ctrl.Antecedent(np.arange(0, 101, 1), 'nem')
oda_boyutu = ctrl.Antecedent(np.arange(10, 101, 1), 'oda_boyutu')

# Çıkış Değişkeni
fan_hizi = ctrl.Consequent(np.arange(0, 101, 1), 'fan_hizi')

# ==========================================================
# Üyelik Fonksiyonları
# ==========================================================

# Sıcaklık
sicaklik['dusuk'] = fuzz.trapmf(sicaklik.universe, [0, 0, 15, 20])
sicaklik['orta'] = fuzz.trapmf(sicaklik.universe, [15, 20, 25, 30])
sicaklik['yuksek'] = fuzz.trapmf(sicaklik.universe, [25, 30, 40, 40])

# Nem
nem['dusuk'] = fuzz.trapmf(nem.universe, [0, 0, 30, 45])
nem['orta'] = fuzz.trapmf(nem.universe, [30, 45, 55, 70])
nem['yuksek'] = fuzz.trapmf(nem.universe, [55, 70, 100, 100])

# Oda Boyutu
oda_boyutu['kucuk'] = fuzz.trapmf(oda_boyutu.universe, [10, 10, 30, 45])
oda_boyutu['orta'] = fuzz.trapmf(oda_boyutu.universe, [30, 45, 55, 70])
oda_boyutu['buyuk'] = fuzz.trapmf(oda_boyutu.universe, [55, 70, 100, 100])

# Fan Hızı
fan_hizi['yavas'] = fuzz.trapmf(fan_hizi.universe, [0, 0, 25, 40])
fan_hizi['orta'] = fuzz.trapmf(fan_hizi.universe, [25, 40, 60, 75])
fan_hizi['hizli'] = fuzz.trapmf(fan_hizi.universe, [60, 75, 100, 100])

# ==========================================================
# Kural Tabanı (27 Kural)
# ==========================================================

labels_temp = ['dusuk', 'orta', 'yuksek']
labels_hum = ['dusuk', 'orta', 'yuksek']
labels_room = ['kucuk', 'orta', 'buyuk']

rules = []
rule_descriptions = []

for t_index, t in enumerate(labels_temp):
    for h_index, h in enumerate(labels_hum):
        for r_index, r in enumerate(labels_room):
            score = t_index + h_index + r_index

            if score <= 2:
                output = 'yavas'
            elif score <= 4:
                output = 'orta'
            else:
                output = 'hizli'

            rule = ctrl.Rule(
                sicaklik[t] & nem[h] & oda_boyutu[r],
                fan_hizi[output]
            )
            rules.append(rule)

            description = (
                f"IF Sıcaklık={t} AND Nem={h} "
                f"AND Oda Boyutu={r} THEN Fan Hızı={output}"
            )
            rule_descriptions.append(description)

# ==========================================================
# Kontrol Sistemi
# ==========================================================

fan_ctrl = ctrl.ControlSystem(rules)

# ==========================================================
# Fan Hızı Hesaplama
# ==========================================================

def calculate_fan_speed(temp_value, humidity_value, room_value):
    simulation = ctrl.ControlSystemSimulation(fan_ctrl)

    simulation.input['sicaklik'] = temp_value
    simulation.input['nem'] = humidity_value
    simulation.input['oda_boyutu'] = room_value

    simulation.compute()

    # Eğer herhangi bir nedenle çıktı oluşmazsa,
    # varsayılan olarak %50 döndür.
    return simulation.output.get('fan_hizi', 50.0)

# ==========================================================
# Aktif Kuralları Listeleme
# ==========================================================

def get_active_rules(temp_value, humidity_value, room_value):
    active = []

    # Giriş üyelik dereceleri
    temp_memberships = {
        'dusuk': fuzz.interp_membership(
            sicaklik.universe, sicaklik['dusuk'].mf, temp_value
        ),
        'orta': fuzz.interp_membership(
            sicaklik.universe, sicaklik['orta'].mf, temp_value
        ),
        'yuksek': fuzz.interp_membership(
            sicaklik.universe, sicaklik['yuksek'].mf, temp_value
        )
    }

    hum_memberships = {
        'dusuk': fuzz.interp_membership(
            nem.universe, nem['dusuk'].mf, humidity_value
        ),
        'orta': fuzz.interp_membership(
            nem.universe, nem['orta'].mf, humidity_value
        ),
        'yuksek': fuzz.interp_membership(
            nem.universe, nem['yuksek'].mf, humidity_value
        )
    }

    room_memberships = {
        'kucuk': fuzz.interp_membership(
            oda_boyutu.universe, oda_boyutu['kucuk'].mf, room_value
        ),
        'orta': fuzz.interp_membership(
            oda_boyutu.universe, oda_boyutu['orta'].mf, room_value
        ),
        'buyuk': fuzz.interp_membership(
            oda_boyutu.universe, oda_boyutu['buyuk'].mf, room_value
        )
    }

    # Tüm kuralları değerlendir
    index = 0
    for t in labels_temp:
        for h in labels_hum:
            for r in labels_room:
                activation = min(
                    temp_memberships[t],
                    hum_memberships[h],
                    room_memberships[r]
                )

                if activation > 0:
                    active.append(
                        (rule_descriptions[index], activation)
                    )

                index += 1

    # Aktivasyona göre sırala
    active.sort(key=lambda x: x[1], reverse=True)

    return active