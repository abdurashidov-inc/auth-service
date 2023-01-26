[Up](../README.md)


### Authentication

User can login via Google OAuth2

```plantuml
@startuml fotocasa_lead_integration
!theme cerulean-outline
 
participant "kodit-backoffice" as backoffice
participant "kodit-proxy" as proxy
participant "kodit-auth" as auth
participant "google-workspace-sdk" as workspace
participant "auth0-sdk" as auth0
participant "opportunity-api" as opportunity
participant "inspector-api" as inspector
database "redis" as redis
 
autonumber
autoactivate off
 
skinparam style strictuml
skinparam responseMessageBelowArrow true
skinparam maxMessageSize 250
skinparam backgroundColor white
skinparam DefaultFontName SansSerif
 
title Authentication

backoffice -> proxy: auth/

@enduml
```