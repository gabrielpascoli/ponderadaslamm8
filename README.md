ponderada 02 "tata"

A aplicação desenvolvida com o intuito de  mapear e navegar por ambientes utilizando pacotes ROS e launchers. A seguir, estão as instruções para compilar o pacote, determinar variáveis necessárias e executar as etapas de mapeamento e navegação.
Compilação do Pacote e Determinação de Variáveis

Para garantir o funcionamento correto do pacote, é necessário compilá-lo e ajustar variáveis para o ROS utilizar suas utilidades mais recentes. Execute os seguintes comandos:

bash

colcon build --packages-select pond2
source install/local_setup.bash  # Se estiver usando zsh, altere para setup.zsh

Tartabot em Ação!

O Tartabot opera em duas etapas: mapeamento e navegação.
Mapeamento do Mundo

A primeira etapa consiste no mapeamento do mundo virtual. Utilize o seguinte comando para executar o launchfile responsável:

bash

ros2 launch pond2 mapping_launch.py

O mapping_launch.py ativa pacotes como turtlebot3_cartographer, turtlebot3_gazebo, turtlebot3_teleop e pond2_teleop, responsáveis pelo mapeamento, simulação do ambiente e robô, controle da movimentação e salvamento do mapa. No terminal turtlebot3_teleop, movimente o robô até preencher completamente o mapa no simulador Rviz. Em seguida, vá para o terminal do pond2_teleop e salve o mapa conforme instruído.
Navegando pelo Mundo

A segunda etapa é a navegação pelo mapa. Execute o seguinte comando no mesmo diretório do mapa salvo:

bash

ros2 launch pond2 tarta_launch.py

O tarta_launch.py ativa pacotes como turtlebot3_navigation2, turtlebot3_gazebo e pond2_tartabot, responsáveis pela navegação, simulação do ambiente e envio de coordenadas de deslocamento.
Vídeo do Tartabot

Confira o funcionamento do Tartabot assistindo ao vídeo a seguir: [https://youtu.be/JIBQrefWRmw]

parte 2 do video [https://youtu.be/khgPnJYyelk]
