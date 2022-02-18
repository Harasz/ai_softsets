from flask import Flask, render_template, request
from wtforms import Form, BooleanField, SelectField, IntegerField
from wtforms.validators import Optional, NumberRange, DataRequired
from alg import get

app = Flask(__name__)


class SampleForm(Form):
    GrLivArea_from = IntegerField('Powierzchnia użytkowa od', [NumberRange(min=-1), DataRequired()])
    GrLivArea_to = IntegerField('Powierzchnia użytkowa do', [NumberRange(min=-1,), DataRequired()])
    LotArea_from = IntegerField('Powierzchnia działki od', [NumberRange(min=-1), DataRequired()])
    LotArea_to = IntegerField('Powierzchnia działki do', [NumberRange(min=-1), DataRequired()])
    GarageArea_from = IntegerField('Powierzchnia garażu od', [NumberRange(min=-1), Optional()], default=0)
    GarageArea_to = IntegerField('Powierzchnia garażu do', [NumberRange(min=-1), Optional()], default=0)
    GarageArea_none = BooleanField('Brak garażu', [Optional()], default=False)
    TotalBsmtSF_from = IntegerField('Powierzchnia piwnicy od', [NumberRange(min=-1), Optional()], default=0)
    TotalBsmtSF_to = IntegerField('Powierzchnia piwnicy do', [NumberRange(min=-1), Optional()], default=0)
    TotalBsmtSF_none = BooleanField('Brak piwnicy', [Optional()], default=False)

    BedroomAbvGr = IntegerField('Ilość pokoi', [NumberRange(min=0), DataRequired()])
    Bathrooms = IntegerField('Ilość łazienek', [NumberRange(min=0), DataRequired()])
    KitchenAbvGr = IntegerField('Ilość kuchni', [NumberRange(min=0), DataRequired()])

    Utilities = SelectField('Przyłącza', [DataRequired()], choices=['all', 'nsw'])
    HeatingWall = BooleanField('Ogrzewanie ścienne', [Optional()], default=False)
    HeatingOthw = BooleanField('Ogrzewanie wodą lub parą', [Optional()], default=False)
    HeatingFloor = BooleanField('Ogrzewanie podłogowe', [Optional()], default=False)
    HeatingGasA = BooleanField('Ogrzewanie gazowe z obiegiem', [Optional()], default=False)
    HeatingGasW = BooleanField('Ogrzewanie gazowe', [Optional()], default=False)
    HeatingGrav = BooleanField('Ogrzewanie grawitacyjne', [Optional()], default=False)
    CentralAir = BooleanField('Klimatyzacja', [Optional()], default=False)
    Fireplaces = BooleanField('Kominek', [Optional()], default=False)
    PoolArea = BooleanField('Basen', [Optional()], default=False)
    Fence = BooleanField('Płot', [Optional()], default=False)
    YearBuilt_from = IntegerField('Rok budowy od', [NumberRange(min=1800, max=2021), Optional()], default=0)
    YearBuilt_to = IntegerField('Rok budowy do', [NumberRange(min=1800, max=2021), Optional()], default=0)
    OverallCond = SelectField('Stan elewacji', [DataRequired()], choices=['5', '4', '3', '2', '1'])
    KitchenQual = SelectField('Stan kuchni', [DataRequired()], choices=['5', '4', '3', '2', '1'])

    StreetP = BooleanField('Dojazd asfaltowy', [Optional()], default=0)
    StreetG = BooleanField('Dojazd żwirowy', [Optional()], default=0)
    PavedDrive1 = BooleanField('Brak chodnika', [Optional()], default=0)
    PavedDriveP = BooleanField('Chodnik brukowany', [Optional()], default=0)
    PavedDrive = BooleanField('Chodnik żwirowany', [Optional()], default=0)

    PavedDrive_p = BooleanField('Procent chodnika', [DataRequired()], default=0)
    Street_p = BooleanField('Procent dojazd', [DataRequired()], default=0)
    KitchenQual_p = BooleanField('Procent kuchnia', [DataRequired()], default=0)
    OverallCond_p = BooleanField('Procent elewacja', [DataRequired()], default=0)
    YearBuilt_p = BooleanField('Procent rok budowy', [DataRequired()], default=0)
    Fence_p = BooleanField('Procent płot', [DataRequired()], default=0)
    PoolArea_p = BooleanField('Procent basen', [DataRequired()], default=0)
    Fireplaces_p = BooleanField('Procent kominek', [DataRequired()], default=0)
    CentralAir_p = BooleanField('Procent klimatyzacja', [DataRequired()], default=0)
    Heating_p = BooleanField('Procent ogrzewanie', [DataRequired()], default=0)
    Utilities_p = BooleanField('Procent przyłącza', [DataRequired()], default=0)
    TotalBsmtSF_p = BooleanField('Procent piwnica', [DataRequired()], default=0)
    GarageArea_p = BooleanField('Procent garaż', [DataRequired()], default=0)
    LotArea_p = BooleanField('Procent działka', [DataRequired()], default=0)
    GrLivArea_p = BooleanField('Procent użytkowa', [DataRequired()], default=0)


def get_int_from_form(key):
    return int(request.form[key])


def get_bool_from_form(key):
    if key in request.form and request.form[key] == 'on':
        return 1
    return 0


def get_per_from_form(key):
    transformed_key = f"{key}_p"
    return int(request.form[transformed_key]) / 100


def get_radio_from_form(key, value):
    if key in request.form and request.form[key] == value:
        return 1
    return 0


def get_translation(data):
    result = {}
    data_values = list(dict(data).values())
    trans = [
            'ID', 'Wielkość działki', 'Ulica asfaltowana', 'Ulica żwirowa', 'Prąd, gaz i woda',
            'Prąd i gaz', 'Stan elewacji (Zniszczona)', 'Stan elewacji (Zła)', 'Stan elewacji (Okej)',
            'Stan elewacji (Dobry)', 'Stan elewacji (Bardzo dobry)',
            'Rok budowy', 'Wielkość piwnicy', 'Ilość łazienek', 'Piec ścienny',
            'Ciepła woda lub para wodna inna niż gaz',
            'Piec grawitacyjny', 'Ogrzewacz gazowy lub ogrzewanie parowe',
            'Piec gazowy z wymuszonym obiegiem ciepłego powietrza', 'Piec podłogowy',
            'Klimatyzacja', 'Wielkość użytkowa', 'Ilość sypialni', 'Ilość kuchni',
            'Stan kuchni (Zniszczona)', 'Stan kuchni (Zła)', 'Stan kuchni (Okej)',
            'Stan kuchni (Dobry)', 'Stan kuchni (Bardzo dobry)', 'Kominek', 'Wielkość garażu', 'Brak chodnika', 'Basen',
            'Chodnik żwirowany', 'Chodnik asfaltowany', 'Płot', 'Cena'
        ]
    for index in range(len(data_values)):
        result[trans[index]] = data_values[index]
    return result


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    form = SampleForm(request.form)
    result = None

    if request.method == 'POST' and form.validate():
        sample = {
            'PMin': [get_int_from_form('LotArea_from')],
            'PMax': [get_int_from_form('LotArea_to')],
            'LotArea': [get_per_from_form('LotArea')],
            'StreetP': [get_bool_from_form('StreetP') * get_per_from_form('Street')],
            'StreetG': [get_bool_from_form('StreetG') * get_per_from_form('Street')],
            'UtilitiesALL': [get_radio_from_form('Utilities', 'all') * get_per_from_form('Utilities')],
            'UtilitiesNSW': [get_radio_from_form('Utilities', 'nsw') * get_per_from_form('Utilities')],
            'OQualPO': [get_radio_from_form('OverallCond', '1') * get_per_from_form('OverallCond')],
            'OQualFA': [get_radio_from_form('OverallCond', '2') * get_per_from_form('OverallCond')],
            'OQualTA': [get_radio_from_form('OverallCond', '3') * get_per_from_form('OverallCond')],
            'OQualGD': [get_radio_from_form('OverallCond', '4') * get_per_from_form('OverallCond')],
            'OQualEX': [get_radio_from_form('OverallCond', '5') * get_per_from_form('OverallCond')],
            'YBMin': [get_int_from_form('YearBuilt_from')],
            'YBMax': [get_int_from_form('YearBuilt_to')],
            'YearBuilt': [get_per_from_form('YearBuilt')],
            'TBSFMin': [get_int_from_form('TotalBsmtSF_from')],
            'TBSFMax': [get_int_from_form('TotalBsmtSF_to')],
            'TotalBsmtSF': [(1 if get_bool_from_form('TotalBsmtSF_none') == 0 else 0) * get_per_from_form('TotalBsmtSF')],
            'Bathrooms': [get_int_from_form('Bathrooms')],
            'HeatingWall': [get_bool_from_form('HeatingWall') * get_per_from_form('Heating')],
            'HeatingOthw': [get_bool_from_form('HeatingOthw') * get_per_from_form('Heating')],
            'HeatingGrav': [get_bool_from_form('HeatingGrav') * get_per_from_form('Heating')],
            'HeatingGasW': [get_bool_from_form('HeatingGasW') * get_per_from_form('Heating')],
            'HeatingGasA': [get_bool_from_form('HeatingGasA') * get_per_from_form('Heating')],
            'HeatingFloor': [get_bool_from_form('HeatingFloor') * get_per_from_form('Heating')],
            'CentralAir': [get_bool_from_form('CentralAir') * get_per_from_form('CentralAir')],
            'GLAMin': [get_int_from_form('GrLivArea_from')],
            'GLAMax': [get_int_from_form('GrLivArea_to')],
            'GrLivArea': [get_per_from_form('GrLivArea')],
            'BedroomAbvGr': [get_int_from_form('BedroomAbvGr')],
            'KitchenAbvGr': [get_int_from_form('KitchenAbvGr')],
            'KitchenQualPO': [get_radio_from_form('KitchenQual', '1') * get_per_from_form('KitchenQual')],
            'KitchenQualFA': [get_radio_from_form('KitchenQual', '2') * get_per_from_form('KitchenQual')],
            'KitchenQualTA': [get_radio_from_form('KitchenQual', '3') * get_per_from_form('KitchenQual')],
            'KitchenQualGD': [get_radio_from_form('KitchenQual', '4') * get_per_from_form('KitchenQual')],
            'KitchenQualEX': [get_radio_from_form('KitchenQual', '5') * get_per_from_form('KitchenQual')],
            'Fireplaces': [get_bool_from_form('Fireplaces') * get_per_from_form('Fireplaces')],
            'GarageMin': [get_int_from_form('GarageArea_from')],
            'GarageMax': [get_int_from_form('GarageArea_to')],
            'GarageArea': [(1 if get_bool_from_form('GarageArea_none') == 0 else 0) * get_per_from_form('GarageArea')],
            'PavedDrive': [get_bool_from_form('PavedDrive') * get_per_from_form('PavedDrive')],
            'PavedDriveP': [get_bool_from_form('PavedDriveP') * get_per_from_form('PavedDrive')],
            'PavedDrive1': [get_bool_from_form('PavedDrive1') * get_per_from_form('PavedDrive')],
            'PoolArea': [get_bool_from_form('PoolArea') * get_per_from_form('PoolArea')],
            'Fence': [get_bool_from_form('Fence') * get_per_from_form('Fence')],
            'BathroomsWeight': [get_per_from_form('Bathrooms')],
            'BedroomAbvGrWeight': [get_per_from_form('BedroomAbvGr')],
            'KitchenAbvGrWeight': [get_per_from_form('KitchenAbvGr')],
        }
        print(sample, flush=True)
        result = get_translation(get(sample))

    return render_template('index.html', form=form, result=result, has_errors=form.validate())
