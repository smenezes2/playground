# Git Instruções

## O que é o git ?

É uma ferramente de versionamento de código.

## O que é o github ?

É uma plataforma de hospedagem de código.


### Conceitos do git 

#### branch

É um estado do código especifico, um conjunto de código criado a partir de outro ramo (branch) 


```bash
$ git branch teste # Cria uma branch com o nome teste
$ git branch # Listagem de branchs atuais
$ git branch -v # Listagem de branchs com seus últimos commits
$ git checkout # Troca de branch
```

**[Link para documentação completa](https://git-scm.com/docs/git-branch/pt_BR)**

#### commit

É um ponto de marcação dentro de uma branch, onde se é possivel voltar ao mesmo lugar pelo commit, pois é gerado um hash.


```bash
$ git commit -m"hello" # Gera um commit com a mensagem `hello`
```


**[Link para documentação completa](https://git-scm.com/docs/git-commit/pt_BR)**


#### push

É passo em que é enviado o código para a sua hospedagem. (Github,Bitbucket,etc...)


```bash
$ git push origin branch_name
```
**[Link para documentação completa](https://git-scm.com/docs/git-push/pt_BR)**


#### checkout

É como trocamos de branch.

```bash
$ git checkout -b"branch_name"

```
**[Link para documentação completa](https://git-scm.com/docs/git-checkout/pt_BR)**


## Ste by step

1. git status
2. git add .
3. git commit -m"Meu segundo commit"
4. git push




