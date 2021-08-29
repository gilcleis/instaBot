# InstaBot



## Sobre <a name = "about"></a>

Projeto em Python para curtir, comentar e seguir usuarios no Instagram

![](./screen.png)

## Inicio <a name = "getting_started"></a>

Projeto desenvolvido em Python 3.8 e usando a biblioteca instapy 0.6


### Instalação

- Clone o repositório com __git clone__ executando o comando:
```
git clone https://github.com/gilcleis/instaBot.git
```
- Acesse o diretorio criado
- Crie uma copia do arqruivo __data_example.yaml__ nomeando para __data.yaml__ 

- acesse as configuracões __data.yaml__ e altere as credenciais de acesso (username e password)

```
username: login              # (instagram user)
password: password          # (instagram password)
friends_interaction: False   # (if True will like friendlist posts,False will avoid create friends session)
do_comments: True           # (if True will comment on user interaction)
do_follow: False             # (if True will follow on user interaction)
user_interact: True         # (if True will interact with user posts)
do_unfollow: false           # (if True will execution unfollow)
do_follow_user_followers : False
friendlist: ['friend1', 'friend2', 'friend3', 'friend4']
hashtags: ['natgeo']
do_hashtags: False
do_stories : True
do_likes : True
do_delimit_likings : True 
targets : ['natgeobrasil', 'discoverybr', 'ed_stafford']
```



- Pronto, execute o script:
```
python instaBot.py
```

