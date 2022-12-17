# VALMISTAJA_TUOTENIMI_MALLI_VUOSI_KUUKAUSI_PÄIVÄ_C_KATEGORIA
products = [
    "PHILIPS_Vedenkeitin_HD4646_2020_09_21_C_1",
    "KENWOOD_Yleiskone_KVL8300S_2015_09_22_C_3",
    "BOSCH_Tehosekoitin_MMB64G5M_2016_05_07_C_3",
    "WHIRLPOOL_Mikroaaltouuni_MCP345WH_2019_01_15_C_1",
    "ROSENLEW_Pakastin_RPP2330_2017_01_29_C_2",
    "ELECTROLUX_Jääkaappi_ERF2114AOW_2017_11_07_C_2"
]

categories = [
    "Muut",
    "Pienlaitteet",
    "Kylmälaitteet",
    "Sekoittimet"
]

# Käsitellään jokainen tuote silmukassa ja jaetaan se osiin
for product in products:
    product = product.split("_")

    print(f"Valmistaja: {product[0]}")
    print(f"Nimi ja malli: {product[1]} ({product[2]})")
    print(f"Kategoria: {categories[int(product[7])]}")
    print(f"Lisäyspäivämäärä: {product[5]}.{product[4]}.{product[3]}")
    print()
