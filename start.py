from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import ChatBot
from chatterbot.response_selection import get_random_response
from chatterbot.storage import storage_adapter
import logging
bot = ChatBot(
    "Go Transa",
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    database_uri='mongodb://192.241.245.34:27017',
    database='gotransa',
    logic_adapters=[
        "chatterbot.logic.MathematicalEvaluation",
        "chatterbot.logic.TimeLogicAdapter",
        "chatterbot.logic.BestMatch"
    ],
    input_adapter="chatterbot.input.TerminalAdapter",
    output_adapter="chatterbot.output.TerminalAdapter"
)

conversation = ["Oi",
"Olá" ,
"Hello",
"E aí?",
"Tudo bem?" ,
"Td bem?",
"Como vai você?",
"Tudo bem e você?",
"Tudo jóia",
"Onde você mora?" ,
"Você tc de onde?",
"Você é de qual cidade?",
"Eu moro em Franca",
"Você mora em qual bairro?",
"Eu moro no Centro",
"Fica perto de onde?",
"Moro perto do shopping",
"Você o que curte fazer?",
"Eu gosto de ler, assistir série no Netflix, barzinho",
"E você?" ,
"E vc?",
"Ah legal",
"Eu gosto de assistir série e filmes , barzinho, jogar futebol",
"Você tem whats app?",
"Tenho sim?",
"Pode me passar?",
"O que você vai aprontar no fds?",
"Ah vai ter uma festa esse fds. Estou pensando em ir...",
"Poderíamos nos encontrar",
"O que você acha?",
"Ah podemos combinar sim",
"Pode ser no sábado?",
"Que horas?",
"Pode ser as 20:30?",
"Combinado",
"Seria onde?",
"Ah pode ser naquele barzinho próximo ao Champagnhat.",
"Pode ser sim",
"O que você faz da vida?",
"Eu trabalho e estudo. E você?",
"Eu trabalho",
"Você trabalha com que?",
"Eu trabalho com tecnologia. E você?",
"Nossa que legal. Eu faço faculdade de Pedagogia e trabalho em uma escola",
"Ah eu pretendo fazer uma pós graduação na minha área",
"Olá, quanto tempo?",
"Olá, sentiu minha falta?",
"ahsheshue senti saudades",
"Ah que bom rsrs",
"Você anda sumida?",
"E aí o que tem feito de bom?",
"Ah tenho trabalhado bastante e curtindo preguiça. E você?",
"Ah eu também",
"Nossa desculpa, preciso sair, daqui a pouco eu volto",
"Ah tudo bem, depois me chama aqui",
"Tenho um ótimo dia",
"Obrigada",
"Você mora com seus pais?",
"Moro com meus pais e irmãos",
"Você tem quantos irmãos?",
"Ah eu tenho 2 irmãos. Sou a caçula rsrs",
"E você namora?",
"Não namoro e você?",
"Eu também não",
"Estou a procura de uma namorada",
"Como foi seu dia?",
"Ah foi bom e o seu?",
"Muito bom, sai com meus amigos no sábado",
"No domingo, estou tranquilo",
"Ah como você é?",
"Tem alguma foto?",
"Ah tenho sim e você?",
"Sim tenho",
"Me manda uma foto que eu mando a minha",
"Está bom, esta aí? ",
"Agora é você?",
"Te enviei",
"Nossa você e muito bonita",
"Obrigado rs"
]

bot.set_trainer(ListTrainer)
bot.train(conversation)

'''
print("Type something to begin...")


while True:
    try:
        # We pass None to this method because the parameter
        # is not used by the TerminalAdapter
        bot_input = bot.get_response(None)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
    '''