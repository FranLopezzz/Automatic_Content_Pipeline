MARCAS = {
    "havanna": {
        "nombre": "Havanna",
        "categoria": "alfajores/dulces",
        "tono": "premium, nostálgico",
        "productos": ["alfajores", "dulce de leche", "café"],
        "claim": "El sabor de la Patagonia"
    },
    "bon_o_bon": {
        "nombre": "Bon o Bon",
        "categoria": "golosinas",
        "tono": "divertido, juvenil",
        "productos": ["bombones", "chocolate"],
        "claim": "El bombón que te hace feliz"
    },
    "topper": {
        "nombre": "Topper",
        "categoria": "indumentaria deportiva",
        "tono": "urbano, accesible",
        "productos": ["zapatillas", "ropa deportiva"],
        "claim": "Tu estilo, tu juego"
    },
    "mantecol": {
        "nombre": "Mantecol",
        "categoria": "golosinas",
        "tono": "nostálgico, familiar",
        "productos": ["postre de maní"],
        "claim": "El postre de la mesa argentina"
    },
    "stella_artois": {
        "nombre": "Stella Artois",
        "categoria": "cerveza",
        "tono": "premium, sofisticado",
        "productos": ["cerveza lager"],
        "claim": "Be Legacy"
    },
    "andes_origen": {
        "nombre": "Andes Origen",
        "categoria": "cerveza",
        "tono": "aventurero, patagónico",
        "productos": ["cerveza artesanal"],
        "claim": "Nacida en la Patagonia"
    },
    "quilmes": {
        "nombre": "Quilmes",
        "categoria": "cerveza",
        "tono": "popular, argentino",
        "productos": ["cerveza lager"],
        "claim": "El sabor del encuentro"
    },
    "fernet_branca": {
        "nombre": "Fernet Branca",
        "categoria": "bebida",
        "tono": "cordobés, social",
        "productos": ["fernet"],
        "claim": "Branca con cola, la mezcla perfecta"
    },
    "taraguei": {
        "nombre": "Yerba Taragüí",
        "categoria": "yerba mate",
        "tono": "tradición, campo",
        "productos": ["yerba mate"],
        "claim": "La yerba de los argentinos"
    },
    "la_serenisima": {
        "nombre": "Dulce de Leche La Serenísima",
        "categoria": "lácteos",
        "tono": "familiar, calidad",
        "productos": ["dulce de leche", "leche", "quesos"],
        "claim": "La calidad es nuestra naturaleza"
    },
    "terrabusi": {
        "nombre": "Alfajores Terrabusi",
        "categoria": "alfajores",
        "tono": "clásico, accesible",
        "productos": ["alfajores", "galletitas"],
        "claim": "El alfajor de todos los días"
    },
    "casancrem": {
        "nombre": "CasanCrem",
        "categoria": "lácteos",
        "tono": "versátil, hogareño",
        "productos": ["queso crema"],
        "claim": "Le ponés CasanCrem y le ponés onda"
    },
    "freddo": {
        "nombre": "Freddo",
        "categoria": "helados",
        "tono": "premium, artesanal",
        "productos": ["helados artesanales"],
        "claim": "Helado como tiene que ser"
    },
    "heinz": {
        "nombre": "Ketchup Heinz",
        "categoria": "condimentos",
        "tono": "icónico, divertido",
        "productos": ["ketchup", "mostaza"],
        "claim": "It has to be Heinz"
    },
    "hellmanns": {
        "nombre": "Mayonesa Hellmann's",
        "categoria": "condimentos",
        "tono": "confiable, cremoso",
        "productos": ["mayonesa", "ketchup"],
        "claim": "El verdadero sabor"
    },
    "la_virginia": {
        "nombre": "Café La Virginia",
        "categoria": "café",
        "tono": "aromático, tradición",
        "productos": ["café molido", "café en grano"],
        "claim": "El café de los argentinos"
    },
    "arcor": {
        "nombre": "Arcor",
        "categoria": "golosinas",
        "tono": "alegre, colorido",
        "productos": ["caramelos", "chocolates", "galletitas"],
        "claim": "Le damos sabor al mundo"
    },
    "cachafaz": {
        "nombre": "Cachafaz",
        "categoria": "alfajores",
        "tono": "artesanal, premium",
        "productos": ["alfajores", "conitos"],
        "claim": "Alfajores de verdad"
    },
    "ser": {
        "nombre": "Ser",
        "categoria": "lácteos",
        "tono": "saludable, liviano",
        "productos": ["yogur", "postres light"],
        "claim": "Ser lo que quieras ser"
    },
    "cindor": {
        "nombre": "Cindor",
        "categoria": "lácteos",
        "tono": "infancia, chocolate",
        "productos": ["leche chocolatada"],
        "claim": "El sabor de siempre"
    }
}


def get_brand(marca_id):
    """Get brand info by ID. Returns None if not found."""
    return MARCAS.get(marca_id)


def get_random_brand(exclude_ids=None):
    """Pick a random brand, optionally excluding recent ones."""
    import random
    available = {k: v for k, v in MARCAS.items() if k not in (exclude_ids or [])}
    if not available:
        available = MARCAS
    marca_id = random.choice(list(available.keys()))
    return marca_id, available[marca_id]


def list_brands():
    """Return list of all brands with IDs."""
    return [{"id": k, **v} for k, v in MARCAS.items()]
