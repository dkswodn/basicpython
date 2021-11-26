inventory = {}

def add_item(item, amount, t_inventory):
    if check_item(item, t_inventory):
        inventory[item] += amount
        print(item+"의 수량은 "+str(t_inventory[item])+"입니다.")
    else:
        t_inventory[item] = amount
        print(item+"이 추가되었습니다.")

def remove_item(item, t_inventory):
    if check_item(item, t_inventory):
        t_inventory[item] = 0
        print(item+"의 수량이 0이 되었습니다.")
    else:
        print(item+"이 존재하지 않습니다.")

def consume_item(item):
    if check_item(item):
        inventory[item] -= 1
        print(item+"이 사용되었습니다. 남은 "+item+"의 수량은 "+str(inventory[item])+"입니다.")
    elif ckeck_item(item):
        inventory[item] = 0
        print(item+"이 0이 되었습니다.")
    elif check_item(item):
        inventory[item] < 1
        print(item+"의 수량이 부족합니다.")
    else:
        print(item+"이 존재하지 않습니다.")
        

def check_item(item, t_inventory):
    return item in t_inventory
def print_menu():
    print("0. 끝내기")
    print("1. 포션 추가")
    print("2. 포션 삭제")
    print("3. 아이템 확인")
    print("4. 아이템 사용")

def use_item():
   while True:
        print_menu()
        option = int(input("메뉴번호를 고르시오)"))
        if option == 0:
            print("종료합니다.")
            break
        elif option == 1:
            new_item = input("아이템을 입력하세요)")
            amount = input("수량을 입력하세요)")
            add_item(new_item, amount, inventory)
        elif option == 2:
            eliminated_item = input("아이템을 입력하세요)")
            remove_item(eliminated_item, inventory)
        elif option == 3:
            print(inventory)
        elif option == 4:
            inventory_item = input("아이템을 입력하세요)")
            consume_item(inventory_item)
        else:
            print("잘못된 번호를입력하셨습니다.")


charactor = {}
select_charactor = None
def new_charactor(name, t_charactor):
    if name in t_charactor:
        print("이미 존재하는 캐릭터의 이름입니다.")
    else:
        inventory = {}
        t_charactor[name] = inventory 

    
def check_charactor(name, t_charactor):
    return name in t_charactor

def print_charactorMenu():
    print("0. 끝내기")
    print("1. 캐릭터 추가")
    print("2. 캐릭터 이름출력")
    print("3. 캐릭터 선택")
    print("4. 캐릭터 인벤토리 조작")

while True:
    print_charactorMenu()
    option = int(input("메뉴를 선택해주세요.)"))
    if option == 0:
        print("종료되었습니다.")
        break
    elif option == 1:
        name = input("캐릭터 이름을 입력하세요.)")
        new_charactor(name, charactor)
    elif option == 2:
        i = 1
        print("######################")
        for name in charactor.keys():
            print(str(i)+". "+name)
            i+=1
        print("######################")
    elif option == 3:
        temp_name = input("선택할 캐릭터의 이름을 입력해주세요.)")
        if check_charactor(temp_name, charactor):
            select_charactor = temp_name
            print(select_charactor+"이 선택되었습니다.")
        else:
            print(temp_name+"은 존재하지 않는 캐릭터입니다.")
        
        
    pass
