import streamlit as st
import matplotlib.pyplot as plt

from fuzzy_controller import (
    calculate_fan_speed,
    get_active_rules,
    sicaklik,
    nem,
    oda_boyutu,
    fan_hizi
)

# ==========================================================
# Sayfa Ayarları
# ==========================================================

st.set_page_config(
    page_title="Akıllı Klima Kontrol Sistemi",
    layout="wide"
)

st.title("Akıllı Klima Kontrol Sistemi")
st.write("Bulanık mantık kullanılarak sıcaklık, nem ve oda boyutuna göre fan hızı hesaplanmaktadır.")

# ==========================================================
# Sidebar Girişleri
# ==========================================================

st.sidebar.header("Giriş Değerleri")

temp = st.sidebar.slider("Sıcaklık (°C)", 0, 40, 25)
humidity = st.sidebar.slider("Nem (%)", 0, 100, 50)
room = st.sidebar.slider("Oda Boyutu (m²)", 10, 100, 50)

# ==========================================================
# Hesapla Butonu
# ==========================================================

if st.sidebar.button("Hesapla"):

    # Sonuç hesapla
    result = calculate_fan_speed(temp, humidity, room)

    # ======================================================
    # Sayısal Sonuç
    # ======================================================

    st.subheader("Fan Hızı Sonucu")
    st.success(f"Fan Hızı: %{result:.2f}")

    # ======================================================
    # Aktif Kurallar
    # ======================================================

    st.subheader("Aktif Kurallar")

    active_rules = get_active_rules(temp, humidity, room)

    if active_rules:
        for rule, activation in active_rules[:10]:
            st.write(f"- {rule} (Aktivasyon: {activation:.3f})")
    else:
        st.write("Aktif kural bulunamadı.")

    # ======================================================
    # Üyelik Fonksiyonları Grafikleri
    # ======================================================

    st.subheader("Üyelik Fonksiyonları")

    # Büyük ve düzenli bir figür oluştur
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # ======================================================
    # 1. SICAKLIK
    # ======================================================

    ax = axes[0, 0]

    for label in ['dusuk', 'orta', 'yuksek']:
        ax.plot(
            sicaklik.universe,
            sicaklik[label].mf,
            linewidth=3,
            label=label.capitalize()
        )

    ax.axvline(
        x=temp,
        color='red',
        linestyle='--',
        linewidth=3,
        label=f'Seçilen: {temp}'
    )

    ax.set_title("Sıcaklık", fontsize=18, fontweight='bold')
    ax.set_xlabel("Değer (°C)", fontsize=12)
    ax.set_ylabel("Üyelik Derecesi", fontsize=12)
    ax.set_xlim(0, 40)
    ax.set_ylim(0, 1.05)
    ax.grid(True, alpha=0.3)
    ax.legend(loc='upper right')

    # ======================================================
    # 2. NEM
    # ======================================================

    ax = axes[0, 1]

    for label in ['dusuk', 'orta', 'yuksek']:
        ax.plot(
            nem.universe,
            nem[label].mf,
            linewidth=3,
            label=label.capitalize()
        )

    ax.axvline(
        x=humidity,
        color='red',
        linestyle='--',
        linewidth=3,
        label=f'Seçilen: {humidity}'
    )

    ax.set_title("Nem", fontsize=18, fontweight='bold')
    ax.set_xlabel("Değer (%)", fontsize=12)
    ax.set_ylabel("Üyelik Derecesi", fontsize=12)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 1.05)
    ax.grid(True, alpha=0.3)
    ax.legend(loc='upper right')

    # ======================================================
    # 3. ODA BOYUTU
    # ======================================================

    ax = axes[1, 0]

    for label in ['kucuk', 'orta', 'buyuk']:
        ax.plot(
            oda_boyutu.universe,
            oda_boyutu[label].mf,
            linewidth=3,
            label=label.capitalize()
        )

    ax.axvline(
        x=room,
        color='red',
        linestyle='--',
        linewidth=3,
        label=f'Seçilen: {room}'
    )

    ax.set_title("Oda Boyutu", fontsize=18, fontweight='bold')
    ax.set_xlabel("Değer (m²)", fontsize=12)
    ax.set_ylabel("Üyelik Derecesi", fontsize=12)
    ax.set_xlim(10, 100)
    ax.set_ylim(0, 1.05)
    ax.grid(True, alpha=0.3)
    ax.legend(loc='upper right')

    # ======================================================
    # 4. FAN HIZI
    # ======================================================

    ax = axes[1, 1]

    for label in ['yavas', 'orta', 'hizli']:
        ax.plot(
            fan_hizi.universe,
            fan_hizi[label].mf,
            linewidth=3,
            label=label.capitalize()
        )

    ax.axvline(
        x=result,
        color='red',
        linestyle='--',
        linewidth=3,
        label=f'Sonuç: {result:.2f}'
    )

    ax.set_title("Fan Hızı", fontsize=18, fontweight='bold')
    ax.set_xlabel("Değer (%)", fontsize=12)
    ax.set_ylabel("Üyelik Derecesi", fontsize=12)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 1.05)
    ax.grid(True, alpha=0.3)
    ax.legend(loc='upper right')

    # ======================================================
    # Grafik Düzeni ve Gösterim
    # ======================================================

    plt.tight_layout()
    st.pyplot(fig)