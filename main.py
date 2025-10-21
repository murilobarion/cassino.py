import time
import random
import os
from rich import print
from rich.panel import Panel

saldo = 1000

def limpar_tela():
    if os.name == 'nt':
        os.system('cls') 
    else:
        os.system('clear')

while True:
    limpar_tela()
    
    print(Panel("Bem-vindo ao BarionBet", title="[bold yellow]BarionBet[/bold yellow]", border_style="green"))
    time.sleep(1)
    
    print('\nVocê começa com $1000. Tente não perder tudo.')
    
    print(f"Seu saldo atual: [bold green]${saldo}[/bold green]")
    
    print(Panel("[bold][1][/bold] Jogar Caça-Níquel\n[bold][2][/bold] Sair", title="O que deseja fazer?", border_style="blue"))
    try:
        escolha = int(input('Sua escolha: '))
    except:
        print("[bold red]Digite 1 ou 2 mané! Voltando..[/bold red]")
        time.sleep(3)
        continue
    
    if escolha == 1:
        time.sleep(0.5)
        print(Panel("[cyan]Ótimo! Quanto você quer arriscar perder?[/cyan]", title="[bold yellow]:slot_machine: Caça-Níquel :slot_machine:[/bold yellow]", border_style="yellow"))
        time.sleep(0.5)
        
        if saldo == 0:
            print("Voce ta zero irmao, tigrinho nao soltou a carta kkkkk")
            time.sleep(3)
            continue
        
        time.sleep(1)
        valor_aposta = int(input('\nDigite aqui o valor da sua aposta: '))
        
        if valor_aposta > saldo:
            print(f"Oloco, voce so tem ${saldo}!")
            print("tenta denovo")
            time.sleep(2)
            continue
            
        elif saldo == 0:
            print('Acabou, zerou tudo sadjajdsa')
            break
        
        else:
            simbolos = ["🍒", "🔔", "💰", "🍋", "💩"]
            
            time.sleep(0.5)
            print(f'\nApostando ${valor_aposta}... Girando a alavanca...\n')
            time.sleep(2)
        
            for i in range(50): 
                s1 = random.choice(simbolos)
                s2 = random.choice(simbolos)
                s3 = random.choice(simbolos)
                print(f"[cyan]Girando...[/cyan] [ {s1} | {s2} | {s3} ]", end="\r", flush=True)
                time.sleep(0.1)
                
            s1_final = random.choice(simbolos)
            s2_final = random.choice(simbolos)
            s3_final = random.choice(simbolos)
            
            print(f"Resultado: [ {s1_final} | {s2_final} | {s3_final} ]\n")
            time.sleep(2)
                
            if s1_final == '💰' and s2_final == '💰' and s3_final == '💰':
                time.sleep(1)
                print("[bold green]JACKPOT!!![/bold green] [yellow]Ganhou 10x a aposta![/yellow]")
                saldo += (valor_aposta * 10)
                    
            elif s1_final == s2_final == s3_final:
                time.sleep(1)
                print("[green]Boa! 3 iguais![/green] Ganhou 3x a aposta!")
                saldo += (valor_aposta * 3)
                    
            else:
                time.sleep(1)
                print("Haha otario, caiu no golpe do [bold orange]TIGRINHO[/bold orange]")
                time.sleep(1)
                print("[red]PERDEU[/red]")
                saldo -= valor_aposta
            
            time.sleep(1)
            print(f"\nSeu novo saldo é: [bold green]${saldo}[/bold green]")
            input("\nPressione [Enter] para continuar...")
            
    elif escolha == 2:
        print('Beleza, fugiu da morte')
        break
    
    else:
        print("Faça uma escolha correta...")
        time.sleep(2)
        continue