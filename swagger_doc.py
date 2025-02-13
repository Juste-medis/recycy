# swagger_doc.py

login_doc = {
    "notes": "Connecte un utilisateur avec email et mot de passe",
    "nickname": "login",
    "parameters": [
        {
            "name": "body",
            "description": "Données de connexion",
            "required": True,
            "allowMultiple": False,
            "dataType": "object",
            "paramType": "body",
            "schema": {
                "email": "string",
                "password": "string"
            }
        }
    ],
    "responseMessages": [
        {"code": 200, "message": "Connexion réussie"},
        {"code": 400, "message": "Erreur de connexion"},
    ]
}

register_doc = {
    "notes": "Inscrit un nouvel utilisateur",
    "nickname": "register",
    "parameters": [
        {
            "name": "body",
            "description": "Données d'inscription",
            "required": True,
            "allowMultiple": False,
            "dataType": "object",
            "paramType": "body",
            "schema": {
                "username": "string",
                "email": "string",
                "password": "string"
            }
        }
    ],
    "responseMessages": [
        {"code": 201, "message": "Inscription réussie"},
        {"code": 400, "message": "Erreur lors de l'inscription"},
    ]
}

logout_doc = {
    "notes": "Déconnecte l'utilisateur (simulé, pas de suppression de token côté serveur)",
    "nickname": "logout",
    "responseMessages": [
        {"code": 200, "message": "Déconnexion réussieddddd"},
    ]
}

# --------------------main route-------------------------------------------------------
upload_doc = {
    "notes": "Permet à l'utilisateur de télécharger un fichier image pour analyse",
    "nickname": "upload",
    "parameters": [
        {
            "name": "Authorization",
            "description": "Token d'authentification JWT. Format: Bearer <token>",
            "required": True,
            "allowMultiple": False,
            "dataType": "string",
            "paramType": "header"
        },
        {
            "name": "file",
            "description": "Le fichier image à traiter",
            "required": True,
            "allowMultiple": False,
            "dataType": "file",
            "paramType": "form"
        }
    ],
    "responseMessages": [
        {"code": 200, "message": "Classification réussie"},
        {"code": 400, "message": "Erreur lors du téléchargement ou traitement du fichier"}
    ]
}

history_doc = {
    "notes": "Récupère l'historique des prédictions pour l'utilisateur connecté",
    "nickname": "history",
    "responseMessages": [
        {"code": 200, "message": "Historique récupéré avec succès"},
        {"code": 401, "message": "Utilisateur non authentifié"}
    ]
}
