# Deze module berekent de emissiewaardes van de bedrijven

from companies_module import is_company_list_complete, companies_l

# Constanten voor emissies per gas
CO2_EMISSION_FACTOR = 1
CH4_EMISSION_FACTOR = 25
NO2_EMISSION_FACTOR = 5
NH3_EMISSION_FACTOR = 1000
FACTOR_FINE = 2


# Berekening van de emissie
def emissions_calculation():
    if not is_company_list_complete():
        return

    for company in companies_l:
        x, y = int(company.get_latitude()), int(company.get_longitude())
        emission_weighted = 0

        for i in range(-2, 3):
            for j in range(-2, 3):
                if 0 <= x + i < 100 and 0 <= y + j < 100:
                    emission1 = company.get_emission1(x + i, y + j)
                    emission2 = company.get_emission2(x + i, y + j)
                    emission3 = company.get_emission3(x + i, y + j)
                    emission4 = company.get_emission4(x + i, y + j)

                    if i == 0 and j == 0:
                        emission_per_m2 = (
                            CO2_EMISSION_FACTOR * emission1 +
                            CH4_EMISSION_FACTOR * emission2 +
                            NO2_EMISSION_FACTOR * emission3 +
                            NH3_EMISSION_FACTOR * emission4
                        )
                    elif abs(i) == 2 or abs(j) == 2:
                        emission_per_m2 = (
                            CO2_EMISSION_FACTOR * emission1 +
                            CH4_EMISSION_FACTOR * emission2 +
                            NO2_EMISSION_FACTOR * emission3 +
                            NH3_EMISSION_FACTOR * emission4
                        ) * 0.25
                    else:
                        emission_per_m2 = (
                            CO2_EMISSION_FACTOR * emission1 +
                            CH4_EMISSION_FACTOR * emission2 +
                            NO2_EMISSION_FACTOR * emission3 +
                            NH3_EMISSION_FACTOR * emission4
                        ) * 0.5

                    emission_weighted += emission_per_m2

        # De berekende waarde wordt in het bedrijfsobject geplaatst
        company.set_calculated_emission(format(emission_weighted, ".2f"))


def calculate_fines():
    for company in companies_l:
        company.calculate_fine()
