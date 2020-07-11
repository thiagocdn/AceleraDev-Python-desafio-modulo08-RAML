doc = '''
#%RAML 1.0


securitySchemes:
    JWT:
        description: JWT Authentication
        type: string
        describedBy:
            headers:
                Authorization:
                    type: string
                    required: true
            responses:
                201:
                    body: 
                        application/json:
                            description: Success token generation
                404:
                    body: 
                        application/json:
                            description: Token not found
        settings:
            roles: []


types:
    Auth:
        type: object
        discriminator: token
        properties:
            token : string
     
    User:
        type: object
        discriminator: user
        properties:
            user_id:
                type: integer
                required: true
                example: 1
            name:
                type: string
                required: true
                example: "Thiago"
            email:
                type: string
                format: email
                required: true
                example: "thiago@example.com"
            last_login:
                type: string
                format: date
                required: true
                example: "2020-07-09"
            group_id: 
                type: integer
                required: true
                example: 1

        example:
            user_id: 1
            name: "Thiago"
            email: "Thiago@example.com"
            last_login: "2020-07-09"
            group_id: 1
                
    Group:
        type: object
        discriminator: group
        properties:
            group_id:
                type: integer
                required: true
                example: 1
            name:
                type: string
                required: true
                example: "Group Name"
        example:
            group_id: 1
            name: "Group Name"
    
    Agent:
        type: object
        discriminator: agent
        properties:
            agent_id:
                type: integer
                required: true
                example: 1
            name:
                type: string
                required: true
                example: "Example"
            status:
                type: boolean
                required: true
                example: true
            environment:
                type: string
                required: true
                example: "Environment"
            version:
                type: string
                required: true
                example: "1.0"
            address:
                type: string
                required: true
                example: "xxx.xx.x.x"
            user_id:
                type: integer
                required: true
                example: 1
        example:
            agent_id: 1
            user_id: 1
            name: "Example"
            status: true
            environment: "Environment"
            version: "1.0"
            address: "xxx.xx.x.x"
    
    
    Event:
        type: object
        discriminator: event
        properties:
            event_id:
                type: integer
                required: true
                example: 1
            agent_id:
                type: integer
                required: true
                example: 1
            level:
                type: string
                required: true
                example: "Critical"
            payload:
                type: string
                required: true
                example: "Example"
            shelved:
                type: boolean
                required: true
                example: true
            date:
                type: string
                format: date-time
                required: true
                example: "2020-07-09 12:00:00"
        example:
            event_id: 1
            agent_id: 1
            level: "Critical"
            payload: "Example"
            shelve: true
            data: "2020-07-09 12:00:00"
                
    Response:
        discriminator: response
        properties:
            message:
                type: string
                example: "Example"
            
/auth/token:
    get:
        description: Get a token
        response:
            200:
                body:
                    type: Response
                example:
                    message: Token gerado
            401:
                body:
                    type: Response
                example:
                    message: Não autorizado
            404:
                body:
                    type: Response
                example:
                    message: Não encontrado
            
    post:
        description: Validate token
        body:
            application/json:
                type: string
                username: string
                password: string
        responses: 
            201:
                body: 
                    application/json:
                        description: Token válido
            400:
                body: 
                    application/json:
                        description: Token inválido
        securedBy: [JWT]
    
           
/agents:
    get:
        description: Listar agentes
        responses: 
            200:
                body:
                    type: Response
                example:
                    message: Listado
            401:
                body:
                    type: Response
                example:
                    message: Não autorizado
            404:
                body:
                    type: Response
                example:
                    message: Não encontrado
        securedBy: [JWT]

    post:
        description: Criar novo agente
        body: 
            application/json:
                example: {
                    "agent_id": 1,
                    "user_id": 1,
                    "name": "Name",
                    "status": true,
                    "environment": "Environment",
                    "version": "1.0",
                    "address": "xxx.xx.x.x"
                    }
        responses: 
            201:
                body:
                    type: Response
                example:
                    message: Criado

            401:
                body:
                    type: Response
                example:
                    message: Não autorizado
        securedBy: [JWT]

    /{id}:
        get:
            description: Listar único agente
            responses: 
                200:
                    body:
                        type: Response
                    example:
                        message: Agente
                401:
                    body:
                        type: Response
                    example:
                        message: Não autorizado
                404:
                    body:
                        type: Response
                    example:
                        message: Não encontrado
            securedBy: [JWT]

        put:
            description: Editar um agente
            responses:
                200:
                    body:
                        type: Response
                    example:
                        message: Editado
                401:
                    body:
                        type: Response
                    example:
                        message: Não autorizado
                404:
                    body:
                        type: Response
                    example:
                        message: Não encontrado
            securedBy: [JWT]

        delete:
            description: Excluir um agente
            responses:
                200:
                    body:
                        type: Response
                    example:
                        message: Deletado
                401:
                    body:
                        type: Response
                    example:
                        message: Não autorizado
                404:
                    body:
                        type: Response
                    example:
                        message: Não encontrado
            securedBy: [JWT]

    /{id}/events:
        get:
            description: Listar eventos de um agente
            responses:
                200:
                    body:
                        type: Event
                    example:
                        message: Listagem
                401:
                    body:
                        type: Response
                    example:
                        message: Não autorizado
                404:
                    body:
                        type: Response
                    example:
                        message: Não encontrado
            securedBy: [JWT]

        post:
            body: 
                application/json:
                    example: {
                        "event_id": 1,
                        "agent_id": 1,
                        "level": "Critical",
                        "data": "Example",
                        "shelve": true
                        }
                201:
                    body:
                        type: Response
                    example:
                        message: Criado
                401:
                    body:
                        type: Response
                    example:
                        message: Não autorizado
                404:
                    body:
                        type: Response
                    example:
                        message: Não encontrado
            securedBy: [JWT]

        put:
            description: Editar um evento
            body:
                type: Event
                
                200:
                    body:
                        type: Response
                    example:
                        message: Editado
                401:
                    body:
                        type: Response
                    example:
                        message: Não autorizado
                404:
                    body:
                        type: Response
                    example:
                        message: Não encontrado
            securedBy: [JWT]

        delete:
            description: Excluir um evento
            body: 
                application/json:
                    properties: 
                        example: {}

                200:
                    body:
                        type: Response
                    example:
                        message: Excluído
                401:
                    body:
                        type: Response
                    example:
                        message: Não autorizado
                404:
                    body:
                        type: Response
                    example:
                        message: Não encontrado
            securedBy: [JWT]
            
    /{id}/events/{id}:
        get:
            description: Listar único evento
            responses:
                200:
                    body:
                        type: Event
                401:
                    body:
                        type: Response
                    example:
                        message: Não autorizado
                404:
                    body:
                        type: Response
                    example:
                        message: Não encontrado
            securedBy: [JWT]
         
        put:
            description: Alterar um evento
            body:
                type: Event
                200:
                    body:
                        type: Response
                    example:
                        message: Alterado
                401:
                    body:
                        type: Response
                    example:
                        message: Não autorizado
                404:
                    body:
                        type: Response
                    example:
                        message: Não encontrado
            securedBy: [JWT]

        delete:
            description: Excluir um evento
            body: 
                application/json:
                    properties: 
                        example: {}
            responses:
                200:
                    body:
                        type: Response
                    example:
                        message: Excluído
                401:
                    body:
                        type: Response
                    example:
                        message: Não autorizado
                404:
                    body:
                        type: Response
                    example:
                        message: Não encontrado
            securedBy: [JWT]


/users:
    get:
        description: Listar usuários
        responses:
            200:
                body:
                    type: User
                example:
                    message: Usuários
        securedBy: [JWT]

    post:
        description: Criar usuário
        body:
            application/json:
                properties:
                    example: {
                        "user_id": 1,
                        "name": "Thiago",
                        "email": "thiago@example.com",
                        "last_login": "2020-07-09",
                        "group_id": 1
                        }
        responses:
            201:
                body:
                    type: User
                example:
                    message: Usuário Criado
            401:
                body:
                    type: Response
                example:
                    message: Não autorizado
            404:
                body:
                    type: Response
                example:
                    message: Não encontrado
        securedBy: [JWT]

    /{id}:
        get:
            description: Listar um usuário
            responses:
                200:
                    body:
                        type: User
                    example:
                        message: Usuário
                401:
                    body:
                        type: Response
                    example:
                        message: Não autorizado
                404:
                    body:
                        type: Response
                    example:
                        message: Não encontrado
            securedBy: [JWT]

        put:
            description: Editar um usuário 
            body:
                type: User
            responses:
                200:
                    body:
                        type: User
                    example:
                        message: Usuário Editado
                401:
                    body:
                        type: Response
                    example:
                        message: Não autorizado
                404:
                    body:
                        type: Response
                    example:
                        message: Não encontrado
            securedBy: [JWT]

        delete:
            description: Excluir um usuário 
            responses:
                200:
                    body:
                        type: Response
                    example:
                        message: Usuário excluído
                401:
                    body:
                        type: Response
                    example:
                        message: Não autorizado
                404:
                    body:
                        type: Response
                    example:
                        message: Não encontrado
            securedBy: [JWT]


/groups:
    get:
        description: Listar grupos
        responses:
            200:
                body:
                    type: Group
                example:
                    message: Grupos
            401:
                body:
                    type: Response
                example:
                    message: Não autorizado
            404:
                body:
                    type: Response
                example:
                    message: Não encontrado
        securedBy: [JWT]

    post:
        description: Criar novo grupo
        body:
            application/json:
                properties: 
                    example: {
                        "group_id": 1,
                        "name": "Nome do Grupo"
                        }
                example: {
                    "group_id": 1,
                    "name": "Nome do Grupo"
                    }
        responses:
            201:
                body:
                    type: Group
                example:
                    message: Grupo criado
            401:
                body:
                    type: Response
                example:
                    message: Não autorizado
            404:
                body:
                    type: Response
                example:
                    message: Não encontrado
        securedBy: [JWT]

    /{id}:
        get:
            description: Listar um grupo
            responses:
                200:
                    body:
                        type: Group
                    example:
                        message: Grupo
                401:
                    body:
                        type: Response
                    example:
                        message: Não autorizado
                404:
                    body:
                        type: Response
                        example:
                            message: Não encontrado
            securedBy: [JWT]

        put:
            description: Editar um grupo
            body:
                type: Group
            responses:
                200:
                    body:
                        type: Group
                    example:
                        message: Grupo editado
                401:
                    body:
                        type: Response
                    example:
                        message: Não autorizado
                404:
                    body:
                        type: Response
                    example:
                        message: Não encontrado
            securedBy: [JWT]

        delete:
            description: Excluir um grupo
            responses:
                204:
                    body:
                        type: Response
                    example:
                        message: Grupo excluído
                401:
                    body:
                        type: Response
                    example:
                        message: Não autorizado
                404:
                    body:
                        type: Response
                    example:
                        message: Não encontrado
            securedBy: [JWT]

'''
