import sys
import random

class Character:
    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, dmg):
        self.hp -= max(0, dmg - self.defense)
        if self.hp < 0:
            self.hp = 0

class Player(Character):
    def __init__(self, name):
        super().__init__(name, 30, 6, 2)
        self.exp = 0

class Enemy(Character):
    pass

def battle(player, enemy):
    print(f"\n你遇到了{enemy.name}！戰鬥開始！")
    while player.is_alive() and enemy.is_alive():
        print(f"你的HP: {player.hp}  {enemy.name}的HP: {enemy.hp}")
        action = input("(A)攻擊  (R)恢復  (Q)逃跑 > ").strip().upper()
        if action == 'A':
            dmg = player.attack + random.randint(-2, 2)
            enemy.take_damage(dmg)
            print(f"你攻擊了{enemy.name}，造成{dmg}點傷害！")
        elif action == 'R':
            heal = random.randint(3, 8)
            player.hp += heal
            print(f"你恢復了{heal}點HP！")
        elif action == 'Q':
            print("你選擇逃跑...\n")
            return False
        else:
            print("無效指令。請重新選擇。")
            continue
        if enemy.is_alive():
            edmg = enemy.attack + random.randint(-1, 1)
            player.take_damage(edmg)
            print(f"{enemy.name}攻擊你，造成{edmg}點傷害！")
    if player.is_alive():
        print(f"你擊敗了{enemy.name}！\n")
        player.exp += 10
        return True
    else:
        print("你被擊敗了...遊戲結束！")
        sys.exit()

def intro():
    print("""
    劍俠江湖
    你是一名初入江湖的年輕劍客，踏上尋找武林祕寶的旅程。
    一切由這裡開始...
    """)

def main():
    intro()
    name = input("請輸入你的名字：")
    player = Player(name)
    print(f"歡迎你，{player.name}！你的冒險即將展開。\n")
    while True:
        print("你來到一個岔路口：")
        print("1. 前往山林小徑")
        print("2. 進入小鎮茶館")
        print("3. 查看角色狀態")
        print("4. 離開遊戲")
        choice = input("請選擇(1-4)：")
        if choice == '1':
            enemy = Enemy("山賊", 18, 5, 1)
            battle(player, enemy)
        elif choice == '2':
            print("你在茶館遇到一位神秘老者，獲得指點，攻擊力+2！")
            player.attack += 2
        elif choice == '3':
            print(f"\n【{player.name}】HP:{player.hp} 攻擊:{player.attack} 防禦:{player.defense} 經驗:{player.exp}\n")
        elif choice == '4':
            print("感謝遊玩，江湖再見！")
            break
        else:
            print("請輸入有效選項。\n")

if __name__ == "__main__":
    main()
