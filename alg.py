import pandas as pd

train = pd.read_csv('train.csv', delimiter=',')
domyt = train[
    ['LotArea', 'Street', 'Utilities', 'OverallCond', 'YearBuilt', 'TotalBsmtSF', 'Heating', 'CentralAir', 'GrLivArea',
     'FullBath', 'HalfBath',
     'BedroomAbvGr', 'KitchenAbvGr', 'KitchenQual', 'Fireplaces', 'GarageArea', 'PavedDrive',
     'PoolArea', 'Fence', 'SalePrice']]
domyt = domyt.fillna("0")
domyt.replace({'Fence': {'MnPrv': 1, 'GdPrv': 1, 'GdWo': 1, 'MnWw': 1}}, inplace=True)
domyt.replace({'Utilities': {'AllPub': 1, 'NoSewr': 2, 'NoSeWa': 0, 'ELO': 0}}, inplace=True)
domyt.replace({'Street': {'Grvl': 0, 'Pave': 1}}, inplace=True)
domyt.replace({'Heating': {'Wall': 0, 'OthW': 1, 'Grav': 2, 'GasW': 3, 'GasA': 4, 'Floor': 5}}, inplace=True)
domyt.replace({'CentralAir': {'N': 0, 'Y': 1}}, inplace=True)
domyt.replace({'KitchenQual': {'Po': 0, 'Fa': 1, 'TA': 2, 'Gd': 3, 'Ex': 4}}, inplace=True)
domyt.replace({'PavedDrive': {'N': 0, 'P': 1, 'Y': 2}}, inplace=True)
domyt.replace({'Fireplaces': {0: 0, 1: 1, 2: 1, 3: 1}}, inplace=True)
domyt.insert(2, 'StreetG', domyt['Street'].copy())
domyt.replace({'StreetG': {0: 1, 1: 0}}, inplace=True)
domyt = domyt.rename(columns={'Street': 'StreetP'})
domyt.insert(4, 'UtilitiesNSW', domyt['Utilities'].copy())
domyt.replace({'UtilitiesNSW': {0: 1, 1: 0}}, inplace=True)
domyt = domyt.rename(columns={'Utilities': 'UtilitiesALL'})
domyt.insert(9, 'HeatingOthw', domyt['Heating'].copy())
domyt.insert(10, 'HeatingGrav', domyt['Heating'].copy())
domyt.insert(11, 'HeatingGasW', domyt['Heating'].copy())
domyt.insert(12, 'HeatingGasA', domyt['Heating'].copy())
domyt.insert(13, 'HeatingFloor', domyt['Heating'].copy())
domyt.replace({'Heating': {0: 1, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}}, inplace=True)
domyt.replace({'HeatingOthw': {0: 0, 1: 1, 2: 0, 3: 0, 4: 0, 5: 0}}, inplace=True)
domyt.replace({'HeatingGrav': {0: 0, 1: 0, 2: 1, 3: 0, 4: 0, 5: 0}}, inplace=True)
domyt.replace({'HeatingGasW': {0: 0, 1: 0, 2: 0, 3: 1, 4: 0, 5: 0}}, inplace=True)
domyt.replace({'HeatingGasA': {0: 0, 1: 0, 2: 0, 3: 0, 4: 1, 5: 0}}, inplace=True)
domyt.replace({'HeatingFloor': {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 1}}, inplace=True)
domyt = domyt.rename(columns={'Heating': 'HeatingWall'})
domyt.insert(25, 'PavedDriveP', domyt['PavedDrive'].copy())
domyt.insert(26, 'PavedDrive1', domyt['PavedDrive'].copy())
domyt.replace({'PavedDrive': {0: 1, 1: 0, 2: 0}}, inplace=True)
domyt.replace({'PavedDriveP': {0: 0, 1: 1, 2: 0}}, inplace=True)
domyt.replace({'PavedDrive1': {0: 0, 1: 0, 2: 1}}, inplace=True)
domyt.replace({'PoolArea': {480: 1, 512: 1, 519: 1, 555: 1, 576: 1, 648: 1, 738: 1}}, inplace=True)
dfa = domyt['FullBath']
dfb = domyt['HalfBath']
dfsumbath = dfa + dfb
domyt = domyt.drop(columns='FullBath')
domyt = domyt.drop(columns='HalfBath')
domyt.insert(8, 'Bathrooms', dfsumbath)
domyt.insert(20, 'KitchenQualFA', domyt['KitchenQual'].copy())
domyt.insert(21, 'KitchenQualTA', domyt['KitchenQual'].copy())
domyt.insert(22, 'KitchenQualGD', domyt['KitchenQual'].copy())
domyt.insert(23, 'KitchenQualEX', domyt['KitchenQual'].copy())
domyt = domyt.rename(columns={'KitchenQual': 'KitchenQualPO'})
domyt.replace({'KitchenQualPO': {0: 1, 1: 0, 2: 0, 3: 0, 4: 0}}, inplace=True)
domyt.replace({'KitchenQualFA': {0: 0, 1: 1, 2: 0, 3: 0, 4: 0}}, inplace=True)
domyt.replace({'KitchenQualTA': {0: 0, 1: 0, 2: 1, 3: 0, 4: 0}}, inplace=True)
domyt.replace({'KitchenQualGD': {0: 0, 1: 0, 2: 0, 3: 1, 4: 0}}, inplace=True)
domyt.replace({'KitchenQualEX': {0: 0, 1: 0, 2: 0, 3: 0, 4: 1}}, inplace=True)
domyt.insert(0, 'index', 1)
domyt['index'] = domyt.index
domyt.insert(6, 'OQualPO', domyt['OverallCond'].copy())
domyt.insert(7, 'OQualFA', domyt['OverallCond'].copy())
domyt.insert(8, 'OQualTA', domyt['OverallCond'].copy())
domyt.insert(9, 'OQualGD', domyt['OverallCond'].copy())
domyt.insert(10, 'OQualEX', domyt['OverallCond'].copy())
domyt = domyt.drop(columns='OverallCond')
domyt.replace({'OQualPO': {1: 1, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}}, inplace=True)
domyt.replace({'OQualFA': {1: 0, 2: 1, 3: 1, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}}, inplace=True)
domyt.replace({'OQualTA': {1: 0, 2: 0, 3: 0, 4: 1, 5: 1, 6: 0, 7: 0, 8: 0, 9: 0}}, inplace=True)
domyt.replace({'OQualGD': {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 1, 7: 1, 8: 0, 9: 0}}, inplace=True)
domyt.replace({'OQualEX': {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 1, 9: 1}}, inplace=True)
wyniktable = domyt.copy()
domyt.to_csv('domy_train.csv', index=False)

val = pd.read_csv('test.csv', delimiter=',')
domyv = val[
    ['LotArea', 'Street', 'Utilities', 'OverallCond', 'YearBuilt', 'TotalBsmtSF', 'Heating', 'CentralAir', 'GrLivArea',
     'FullBath', 'HalfBath',
     'BedroomAbvGr', 'KitchenAbvGr', 'KitchenQual', 'Fireplaces', 'GarageArea', 'PavedDrive',
     'PoolArea', 'Fence']]
domyv = domyv.fillna('0')
domyv.replace({'Fence': {'0': 0, 'MnPrv': 1, 'GdPrv': 1, 'GdWo': 1, 'MnWw': 1}}, inplace=True)
domyv.replace({'Utilities': {'AllPub': 3, 'NoSewr': 2, 'NoSeWa': 1, 'ELO': 0}}, inplace=True)
domyv.replace({'Street': {'Grvl': 0, 'Pave': 1}}, inplace=True)
domyv.replace({'Heating': {'Wall': 0, 'OthW': 1, 'Grav': 2, 'GasW': 3, 'GasA': 4, 'Floor': 5}}, inplace=True)
domyv.replace({'CentralAir': {'N': 0, 'Y': 1}}, inplace=True)
domyv.replace({'KitchenQual': {'Po': 0, 'Fa': 1, 'TA': 2, 'Gd': 3, 'Ex': 4}}, inplace=True)
domyv.replace({'PavedDrive': {'N': 0, 'P': 1, 'Y': 2}}, inplace=True)

domyv.to_csv('domy_val.csv', index=False)
domyt['Fence'] = domyt['Fence'].astype(str).astype(int)
domyv['Fence'] = domyv['Fence'].astype(str).astype(int)

domyv['Utilities'] = domyv['Utilities'].astype(str).astype(int)
domyv['KitchenQual'] = domyv['KitchenQual'].astype(str).astype(int)
domyv['TotalBsmtSF'] = domyv['TotalBsmtSF'].astype(str).astype(float)
domyv['GarageArea'] = domyv['GarageArea'].astype(str).astype(float)


class ProcessD:
    def __init__(self, sample_house, data_set, house_pick_table):
        self.sample = sample_house
        self.X = data_set
        self.pick_house = house_pick_table
        self.picked_house = self.sample.iloc[0]

    def get_data(self, x, y, column_name):
        temp1 = 0
        for i in self.X.loc[:, column_name]:
            if x <= i <= y:
                self.X.loc[temp1, column_name] = 1
            else:
                self.X.loc[temp1, column_name] = 0
            temp1 += 1

    @staticmethod
    def vector_sum(v1, v2):
        v_sum = 0
        for i in v1.keys():
            v_sum += v1[i] * v2[i]
        return v_sum

    def sum_list(self):
        sum_list = []
        for i in range(len(self.X)):
            sum_list.append([self.X.iloc[i], self.vector_sum(self.sample.iloc[0], self.X.iloc[i])])
        ma = max(sum_list, key=lambda x: x[1])
        return ma[0]

    def unpack(self):
        p_min = self.sample.iloc[0, 0]
        PMax = self.sample.iloc[0, 1]
        YBMin = self.sample.iloc[0, 12]
        YBMax = self.sample.iloc[0, 13]
        t_b_sf_min = self.sample.iloc[0, 15]
        t_b_sf_max = self.sample.iloc[0, 16]
        Bathrooms = self.sample.iloc[0, 18]
        GLAMin = self.sample.iloc[0, 26]
        GLAMax = self.sample.iloc[0, 27]
        Bedrooms = self.sample.iloc[0, 29]
        Kitchen = self.sample.iloc[0, 30]
        GarageMin = self.sample.iloc[0, 37]
        GarageMax = self.sample.iloc[0, 38]
        col_drop = [0, 1, 12, 13, 15, 16, 26, 27, 37, 38]
        self.sample.drop(self.sample.columns[col_drop], axis=1, inplace=True)
        self.get_data(p_min, PMax, 'LotArea')
        self.get_data(GarageMin, GarageMax, 'GarageArea')
        self.get_data(Bedrooms, 999, 'BedroomAbvGr')
        self.get_data(Kitchen, 999, 'KitchenAbvGr')
        self.get_data(Bathrooms, 999, 'Bathrooms')
        self.get_data(GLAMin, GLAMax, 'GrLivArea')
        self.get_data(t_b_sf_min, t_b_sf_max, 'TotalBsmtSF')
        self.get_data(YBMin, YBMax, 'YearBuilt')
        self.sample.loc[0, 'BedroomAbvGr'] = self.sample.loc[0, 'BedroomAbvGrWeight']
        self.sample.loc[0, 'Bathrooms'] = self.sample.loc[0, 'BathroomsWeight']
        self.sample.loc[0, 'KitchenAbvGr'] = self.sample.loc[0, 'KitchenAbvGrWeight']
        self.sample = self.sample.drop(columns='BathroomsWeight')
        self.sample = self.sample.drop(columns='BedroomAbvGrWeight')
        self.sample = self.sample.drop(columns='KitchenAbvGrWeight')

    def show(self):
        index = int(self.picked_house['index'])
        return self.pick_house.iloc[index]

    def start(self):
        self.unpack()
        self.picked_house = self.sum_list()
        return self.show()


def get(sample):
    sample = pd.DataFrame(data=sample)
    return ProcessD(sample, domyt, wyniktable).start()
