const express = require('express');
const router = express.Router();

const MARCAS = [
  { id: 'havanna', nombre: 'Havanna', categoria: 'alfajores/dulces', tono: 'premium, nostálgico' },
  { id: 'bon_o_bon', nombre: 'Bon o Bon', categoria: 'golosinas', tono: 'divertido, juvenil' },
  { id: 'topper', nombre: 'Topper', categoria: 'indumentaria deportiva', tono: 'urbano, accesible' },
  { id: 'mantecol', nombre: 'Mantecol', categoria: 'golosinas', tono: 'nostálgico, familiar' },
  { id: 'stella_artois', nombre: 'Stella Artois', categoria: 'cerveza', tono: 'premium, sofisticado' },
  { id: 'andes_origen', nombre: 'Andes Origen', categoria: 'cerveza', tono: 'aventurero, patagónico' },
  { id: 'quilmes', nombre: 'Quilmes', categoria: 'cerveza', tono: 'popular, argentino' },
  { id: 'fernet_branca', nombre: 'Fernet Branca', categoria: 'bebida', tono: 'cordobés, social' },
  { id: 'taraguei', nombre: 'Yerba Taragüí', categoria: 'yerba mate', tono: 'tradición, campo' },
  { id: 'la_serenisima', nombre: 'Dulce de Leche La Serenísima', categoria: 'lácteos', tono: 'familiar, calidad' },
  { id: 'terrabusi', nombre: 'Alfajores Terrabusi', categoria: 'alfajores', tono: 'clásico, accesible' },
  { id: 'casancrem', nombre: 'CasanCrem', categoria: 'lácteos', tono: 'versátil, hogareño' },
  { id: 'freddo', nombre: 'Freddo', categoria: 'helados', tono: 'premium, artesanal' },
  { id: 'heinz', nombre: 'Ketchup Heinz', categoria: 'condimentos', tono: 'icónico, divertido' },
  { id: 'hellmanns', nombre: "Mayonesa Hellmann's", categoria: 'condimentos', tono: 'confiable, cremoso' },
  { id: 'la_virginia', nombre: 'Café La Virginia', categoria: 'café', tono: 'aromático, tradición' },
  { id: 'arcor', nombre: 'Arcor', categoria: 'golosinas', tono: 'alegre, colorido' },
  { id: 'cachafaz', nombre: 'Cachafaz', categoria: 'alfajores', tono: 'artesanal, premium' },
  { id: 'ser', nombre: 'Ser', categoria: 'lácteos', tono: 'saludable, liviano' },
  { id: 'cindor', nombre: 'Cindor', categoria: 'lácteos', tono: 'infancia, chocolate' }
];

router.get('/', (req, res) => {
  res.json(MARCAS);
});

// Export MARCAS for use in other modules
router.MARCAS = MARCAS;

module.exports = router;
