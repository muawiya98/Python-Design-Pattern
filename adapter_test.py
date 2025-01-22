from sardeena_adapter import SardeenaAdapter
from enemy_plan import EnemyPlan
from enemy_tank import EnemyTank
from sardeena import Sardeena

class AdapterTest:
    def run(self):
        enemies = []
        enemies.append(EnemyPlan())
        enemies.append(EnemyTank())
        enemies.append(EnemyTank())
        enemies.append(SardeenaAdapter(Sardeena()))

        for enemy in enemies:
            print(50*"*")
            enemy.fireCannons()
            enemy.refillBanzeen()

if __name__ == '__main__':
    adapter_test = AdapterTest()
    adapter_test.run()