import schedule
import time as tm
from datetime import time
from schedule import repeat, every

@repeat(every().second) # Para deixar o código mais organizado. Usar o @repeat antes da função. Precisa importá-la.
def tarefa():
    print("Teste")

# schedule.every(5).seconds.do(tarefa) # Nessa parte do código, posso por para rodar em dias, semanas, mês...
#schedule.every().hour.at(":57").do(tarefa) # Rodar a auomação a cada hora em um determinado minuto.
# schedule.every().second.until(time(19, 4)).do(tarefa) # Para rodar a automação até um determinado horário programado. Ex.: No horário de trabalho.


while True:
    schedule.run_pending()
    tm.sleep(1)