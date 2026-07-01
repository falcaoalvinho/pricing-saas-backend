# Pricing API [WORK in PROGRESS]

### Backend para gerenciamento de produtos e precificação baseada em margem e custos
 
Atualmente estou reformulando a modelagem das entidades do banco de dados, na nova distribuição para além de produtos e usuários, optei por incluir as entidades Organization, Membership e Subscription, com elas passei a agrupar os produtos e usuários, e pude começar a rascunhar a estrutura de um SaaS mais robusto do que a proposta original. 

O projeto ainda segue um viés Build to Lern, mas no formato atual segue mais próximo do que poderia encontrar em um cenário real.h

## Stack

- FastAPI
- PostgreSQL
- SQLAlchemy
- Docker

## Arquitetura

Router → Service → Repository → Database

## Rodando o projeto (testar depois)

docker compose up --build

API disponível em (sem um deploy de fato por hora):
http://localhost:8000/docs
