import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Girişler
sicaklik = ctrl.Antecedent(np.arange(0, 51, 1), 'sicaklik')
hava_nemi = ctrl.Antecedent(np.arange(0, 101, 1), 'hava_nemi')
toprak_nemi = ctrl.Antecedent(np.arange(0, 101, 1), 'toprak_nemi')
isik = ctrl.Antecedent(np.arange(0, 10001, 1), 'isik')
co2 = ctrl.Antecedent(np.arange(300, 1501, 1), 'co2')

# Çıkışlar
isitma = ctrl.Consequent(np.arange(0, 101, 1), 'isitma')
sulama = ctrl.Consequent(np.arange(0, 101, 1), 'sulama')

# Üyelik fonksiyonları (otomatik)
sicaklik.automf(3)
hava_nemi.automf(3)
toprak_nemi.automf(3)
isik.automf(3)
co2.automf(3)
isitma.automf(3)
sulama.automf(3)

# Kurallar (örnek)
rule1 = ctrl.Rule(sicaklik['poor'] | toprak_nemi['poor'], isitma['good'])
rule2 = ctrl.Rule(hava_nemi['good'] & isik['average'], sulama['average'])
rule3 = ctrl.Rule(co2['poor'], isitma['average'])  # ← تمت إضافة قاعدة لـ co2

# Kontrol sistemi
sera_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
sera_sim = ctrl.ControlSystemSimulation(sera_ctrl)

def run_fuzzy_logic(s, hn, tn, i, c):
    sera_sim.input['sicaklik'] = s
    sera_sim.input['hava_nemi'] = hn
    sera_sim.input['toprak_nemi'] = tn
    sera_sim.input['isik'] = i
    sera_sim.input['co2'] = c
    sera_sim.compute()
    return sera_sim.output['isitma'], sera_sim.output['sulama']
