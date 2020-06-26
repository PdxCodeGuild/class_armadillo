
let pokedex = new Vue({
    el: '#pokedex-container',
    data: {
        pokemon: [],
        allTypes: [
            'normal', 'fire', 'water', 'grass', 'electric', 'ice', 'fighting', 'poison', 
            'ground', 'flying', 'psychic', 'bug', 'rock', 'ghost', 'dragon'
        ],
        pokemonSet: [],
        pokemonPage: [],
        currentPokemon: null,

        query: '',
        queryType: 'name',
        pageNumber: 1,
        perPage: 5,
    },
    methods: {
        update: function () {
            this.search()
        },
        search: function () {
            this.pokemonSet = []
            this.pokemonPage = []
            this.currentPokemon = {}

            if(this.query == ''){
                return
            }

            for (let i = 0; i < this.pokemon.length; i++) {
                if(this.queryType == 'name'){
                    if(this.pokemon[i][this.queryType].includes(this.query)){
                        this.pokemonSet.push(this.pokemon[i])
                    }
                } else if(this.queryType == 'types'){

                    console.log(this.pokemon[i]['types'])
                    for(let type of this.pokemon[i]['types']){
                        if(type.includes(this.query)){
                            this.pokemonSet.push(this.pokemon[i])
                        }
                    }
                } else if(this.queryType == 'number'){
                    if(this.pokemon[i][this.queryType] == this.query){
                        this.pokemonSet.push(this.pokemon[i])
                    }
                }
            }
            if(this.pokemonSet.length == 1){
                this.currentPokemon = this.pokemonSet[0]
            } else if(this.pokemonSet.length < this.perPage){
                this.pokemonPage = this.pokemonSet
            } else {
                this.getPage()
            }
        },
        getPage: function(){
            let start = (this.pageNumber - 1) * this.perPage
            let end = start + this.perPage
            this.pokemonPage = this.pokemonSet.slice(start, end)
            console.log(this.pokemonPage)
        },
        nextPage: function () {

        },
        prevPage: function () {

        }
    },
    created: function () {
        // Yes, I know this is gross
        this.pokemon = [
                {
                    "number": 1,
                    "name": "bulbasaur",
                    "height": 7,
                    "weight": 69,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/1.png",
                    "types": [
                        "poison",
                        "grass"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/bulbasaur"
                },
                {
                    "number": 2,
                    "name": "ivysaur",
                    "height": 10,
                    "weight": 130,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/2.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/2.png",
                    "types": [
                        "poison",
                        "grass"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/ivysaur"
                },
                {
                    "number": 3,
                    "name": "venusaur",
                    "height": 20,
                    "weight": 1000,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/3.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/3.png",
                    "types": [
                        "poison",
                        "grass"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/venusaur"
                },
                {
                    "number": 4,
                    "name": "charmander",
                    "height": 6,
                    "weight": 85,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/4.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/4.png",
                    "types": [
                        "fire"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/charmander"
                },
                {
                    "number": 5,
                    "name": "charmeleon",
                    "height": 11,
                    "weight": 190,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/5.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/5.png",
                    "types": [
                        "fire"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/charmeleon"
                },
                {
                    "number": 6,
                    "name": "charizard",
                    "height": 17,
                    "weight": 905,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/6.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/6.png",
                    "types": [
                        "flying",
                        "fire"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/charizard"
                },
                {
                    "number": 7,
                    "name": "squirtle",
                    "height": 5,
                    "weight": 90,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/7.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/7.png",
                    "types": [
                        "water"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/squirtle"
                },
                {
                    "number": 8,
                    "name": "wartortle",
                    "height": 10,
                    "weight": 225,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/8.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/8.png",
                    "types": [
                        "water"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/wartortle"
                },
                {
                    "number": 9,
                    "name": "blastoise",
                    "height": 16,
                    "weight": 855,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/9.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/9.png",
                    "types": [
                        "water"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/blastoise"
                },
                {
                    "number": 10,
                    "name": "caterpie",
                    "height": 3,
                    "weight": 29,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/10.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/10.png",
                    "types": [
                        "bug"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/caterpie"
                },
                {
                    "number": 11,
                    "name": "metapod",
                    "height": 7,
                    "weight": 99,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/11.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/11.png",
                    "types": [
                        "bug"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/metapod"
                },
                {
                    "number": 12,
                    "name": "butterfree",
                    "height": 11,
                    "weight": 320,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/12.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/12.png",
                    "types": [
                        "flying",
                        "bug"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/butterfree"
                },
                {
                    "number": 13,
                    "name": "weedle",
                    "height": 3,
                    "weight": 32,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/13.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/13.png",
                    "types": [
                        "poison",
                        "bug"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/weedle"
                },
                {
                    "number": 14,
                    "name": "kakuna",
                    "height": 6,
                    "weight": 100,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/14.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/14.png",
                    "types": [
                        "poison",
                        "bug"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/kakuna"
                },
                {
                    "number": 15,
                    "name": "beedrill",
                    "height": 10,
                    "weight": 295,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/15.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/15.png",
                    "types": [
                        "poison",
                        "bug"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/beedrill"
                },
                {
                    "number": 16,
                    "name": "pidgey",
                    "height": 3,
                    "weight": 18,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/16.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/16.png",
                    "types": [
                        "flying",
                        "normal"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/pidgey"
                },
                {
                    "number": 17,
                    "name": "pidgeotto",
                    "height": 11,
                    "weight": 300,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/17.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/17.png",
                    "types": [
                        "flying",
                        "normal"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/pidgeotto"
                },
                {
                    "number": 18,
                    "name": "pidgeot",
                    "height": 15,
                    "weight": 395,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/18.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/18.png",
                    "types": [
                        "flying",
                        "normal"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/pidgeot"
                },
                {
                    "number": 19,
                    "name": "rattata",
                    "height": 3,
                    "weight": 35,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/19.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/19.png",
                    "types": [
                        "normal"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/rattata"
                },
                {
                    "number": 20,
                    "name": "raticate",
                    "height": 7,
                    "weight": 185,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/20.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/20.png",
                    "types": [
                        "normal"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/raticate"
                },
                {
                    "number": 21,
                    "name": "spearow",
                    "height": 3,
                    "weight": 20,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/21.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/21.png",
                    "types": [
                        "flying",
                        "normal"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/spearow"
                },
                {
                    "number": 22,
                    "name": "fearow",
                    "height": 12,
                    "weight": 380,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/22.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/22.png",
                    "types": [
                        "flying",
                        "normal"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/fearow"
                },
                {
                    "number": 23,
                    "name": "ekans",
                    "height": 20,
                    "weight": 69,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/23.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/23.png",
                    "types": [
                        "poison"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/ekans"
                },
                {
                    "number": 24,
                    "name": "arbok",
                    "height": 35,
                    "weight": 650,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/24.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/24.png",
                    "types": [
                        "poison"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/arbok"
                },
                {
                    "number": 25,
                    "name": "pikachu",
                    "height": 4,
                    "weight": 60,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/25.png",
                    "types": [
                        "electric"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/pikachu"
                },
                {
                    "number": 26,
                    "name": "raichu",
                    "height": 8,
                    "weight": 300,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/26.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/26.png",
                    "types": [
                        "electric"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/raichu"
                },
                {
                    "number": 27,
                    "name": "sandshrew",
                    "height": 6,
                    "weight": 120,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/27.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/27.png",
                    "types": [
                        "ground"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/sandshrew"
                },
                {
                    "number": 28,
                    "name": "sandslash",
                    "height": 10,
                    "weight": 295,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/28.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/28.png",
                    "types": [
                        "ground"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/sandslash"
                },
                {
                    "number": 29,
                    "name": "nidoran-f",
                    "height": 4,
                    "weight": 70,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/29.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/29.png",
                    "types": [
                        "poison"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/nidoran-f"
                },
                {
                    "number": 30,
                    "name": "nidorina",
                    "height": 8,
                    "weight": 200,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/30.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/30.png",
                    "types": [
                        "poison"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/nidorina"
                },
                {
                    "number": 31,
                    "name": "nidoqueen",
                    "height": 13,
                    "weight": 600,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/31.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/31.png",
                    "types": [
                        "ground",
                        "poison"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/nidoqueen"
                },
                {
                    "number": 32,
                    "name": "nidoran-m",
                    "height": 5,
                    "weight": 90,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/32.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/32.png",
                    "types": [
                        "poison"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/nidoran-m"
                },
                {
                    "number": 33,
                    "name": "nidorino",
                    "height": 9,
                    "weight": 195,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/33.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/33.png",
                    "types": [
                        "poison"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/nidorino"
                },
                {
                    "number": 34,
                    "name": "nidoking",
                    "height": 14,
                    "weight": 620,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/34.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/34.png",
                    "types": [
                        "ground",
                        "poison"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/nidoking"
                },
                {
                    "number": 35,
                    "name": "clefairy",
                    "height": 6,
                    "weight": 75,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/35.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/35.png",
                    "types": [
                        "fairy"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/clefairy"
                },
                {
                    "number": 36,
                    "name": "clefable",
                    "height": 13,
                    "weight": 400,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/36.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/36.png",
                    "types": [
                        "fairy"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/clefable"
                },
                {
                    "number": 37,
                    "name": "vulpix",
                    "height": 6,
                    "weight": 99,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/37.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/37.png",
                    "types": [
                        "fire"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/vulpix"
                },
                {
                    "number": 38,
                    "name": "ninetales",
                    "height": 11,
                    "weight": 199,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/38.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/38.png",
                    "types": [
                        "fire"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/ninetales"
                },
                {
                    "number": 39,
                    "name": "jigglypuff",
                    "height": 5,
                    "weight": 55,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/39.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/39.png",
                    "types": [
                        "fairy",
                        "normal"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/jigglypuff"
                },
                {
                    "number": 40,
                    "name": "wigglytuff",
                    "height": 10,
                    "weight": 120,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/40.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/40.png",
                    "types": [
                        "fairy",
                        "normal"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/wigglytuff"
                },
                {
                    "number": 41,
                    "name": "zubat",
                    "height": 8,
                    "weight": 75,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/41.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/41.png",
                    "types": [
                        "flying",
                        "poison"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/zubat"
                },
                {
                    "number": 42,
                    "name": "golbat",
                    "height": 16,
                    "weight": 550,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/42.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/42.png",
                    "types": [
                        "flying",
                        "poison"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/golbat"
                },
                {
                    "number": 43,
                    "name": "oddish",
                    "height": 5,
                    "weight": 54,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/43.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/43.png",
                    "types": [
                        "poison",
                        "grass"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/oddish"
                },
                {
                    "number": 44,
                    "name": "gloom",
                    "height": 8,
                    "weight": 86,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/44.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/44.png",
                    "types": [
                        "poison",
                        "grass"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/gloom"
                },
                {
                    "number": 45,
                    "name": "vileplume",
                    "height": 12,
                    "weight": 186,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/45.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/45.png",
                    "types": [
                        "poison",
                        "grass"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/vileplume"
                },
                {
                    "number": 46,
                    "name": "paras",
                    "height": 3,
                    "weight": 54,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/46.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/46.png",
                    "types": [
                        "grass",
                        "bug"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/paras"
                },
                {
                    "number": 47,
                    "name": "parasect",
                    "height": 10,
                    "weight": 295,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/47.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/47.png",
                    "types": [
                        "grass",
                        "bug"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/parasect"
                },
                {
                    "number": 48,
                    "name": "venonat",
                    "height": 10,
                    "weight": 300,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/48.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/48.png",
                    "types": [
                        "poison",
                        "bug"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/venonat"
                },
                {
                    "number": 49,
                    "name": "venomoth",
                    "height": 15,
                    "weight": 125,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/49.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/49.png",
                    "types": [
                        "poison",
                        "bug"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/venomoth"
                },
                {
                    "number": 50,
                    "name": "diglett",
                    "height": 2,
                    "weight": 8,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/50.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/50.png",
                    "types": [
                        "ground"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/diglett"
                },
                {
                    "number": 51,
                    "name": "dugtrio",
                    "height": 7,
                    "weight": 333,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/51.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/51.png",
                    "types": [
                        "ground"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/dugtrio"
                },
                {
                    "number": 52,
                    "name": "meowth",
                    "height": 4,
                    "weight": 42,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/52.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/52.png",
                    "types": [
                        "normal"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/meowth"
                },
                {
                    "number": 53,
                    "name": "persian",
                    "height": 10,
                    "weight": 320,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/53.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/53.png",
                    "types": [
                        "normal"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/persian"
                },
                {
                    "number": 54,
                    "name": "psyduck",
                    "height": 8,
                    "weight": 196,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/54.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/54.png",
                    "types": [
                        "water"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/psyduck"
                },
                {
                    "number": 55,
                    "name": "golduck",
                    "height": 17,
                    "weight": 766,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/55.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/55.png",
                    "types": [
                        "water"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/golduck"
                },
                {
                    "number": 56,
                    "name": "mankey",
                    "height": 5,
                    "weight": 280,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/56.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/56.png",
                    "types": [
                        "fighting"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/mankey"
                },
                {
                    "number": 57,
                    "name": "primeape",
                    "height": 10,
                    "weight": 320,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/57.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/57.png",
                    "types": [
                        "fighting"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/primeape"
                },
                {
                    "number": 58,
                    "name": "growlithe",
                    "height": 7,
                    "weight": 190,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/58.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/58.png",
                    "types": [
                        "fire"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/growlithe"
                },
                {
                    "number": 59,
                    "name": "arcanine",
                    "height": 19,
                    "weight": 1550,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/59.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/59.png",
                    "types": [
                        "fire"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/arcanine"
                },
                {
                    "number": 60,
                    "name": "poliwag",
                    "height": 6,
                    "weight": 124,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/60.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/60.png",
                    "types": [
                        "water"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/poliwag"
                },
                {
                    "number": 61,
                    "name": "poliwhirl",
                    "height": 10,
                    "weight": 200,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/61.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/61.png",
                    "types": [
                        "water"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/poliwhirl"
                },
                {
                    "number": 62,
                    "name": "poliwrath",
                    "height": 13,
                    "weight": 540,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/62.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/62.png",
                    "types": [
                        "fighting",
                        "water"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/poliwrath"
                },
                {
                    "number": 63,
                    "name": "abra",
                    "height": 9,
                    "weight": 195,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/63.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/63.png",
                    "types": [
                        "psychic"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/abra"
                },
                {
                    "number": 64,
                    "name": "kadabra",
                    "height": 13,
                    "weight": 565,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/64.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/64.png",
                    "types": [
                        "psychic"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/kadabra"
                },
                {
                    "number": 65,
                    "name": "alakazam",
                    "height": 15,
                    "weight": 480,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/65.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/65.png",
                    "types": [
                        "psychic"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/alakazam"
                },
                {
                    "number": 66,
                    "name": "machop",
                    "height": 8,
                    "weight": 195,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/66.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/66.png",
                    "types": [
                        "fighting"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/machop"
                },
                {
                    "number": 67,
                    "name": "machoke",
                    "height": 15,
                    "weight": 705,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/67.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/67.png",
                    "types": [
                        "fighting"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/machoke"
                },
                {
                    "number": 68,
                    "name": "machamp",
                    "height": 16,
                    "weight": 1300,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/68.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/68.png",
                    "types": [
                        "fighting"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/machamp"
                },
                {
                    "number": 69,
                    "name": "bellsprout",
                    "height": 7,
                    "weight": 40,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/69.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/69.png",
                    "types": [
                        "poison",
                        "grass"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/bellsprout"
                },
                {
                    "number": 70,
                    "name": "weepinbell",
                    "height": 10,
                    "weight": 64,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/70.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/70.png",
                    "types": [
                        "poison",
                        "grass"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/weepinbell"
                },
                {
                    "number": 71,
                    "name": "victreebel",
                    "height": 17,
                    "weight": 155,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/71.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/71.png",
                    "types": [
                        "poison",
                        "grass"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/victreebel"
                },
                {
                    "number": 72,
                    "name": "tentacool",
                    "height": 9,
                    "weight": 455,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/72.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/72.png",
                    "types": [
                        "poison",
                        "water"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/tentacool"
                },
                {
                    "number": 73,
                    "name": "tentacruel",
                    "height": 16,
                    "weight": 550,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/73.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/73.png",
                    "types": [
                        "poison",
                        "water"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/tentacruel"
                },
                {
                    "number": 74,
                    "name": "geodude",
                    "height": 4,
                    "weight": 200,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/74.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/74.png",
                    "types": [
                        "ground",
                        "rock"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/geodude"
                },
                {
                    "number": 75,
                    "name": "graveler",
                    "height": 10,
                    "weight": 1050,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/75.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/75.png",
                    "types": [
                        "ground",
                        "rock"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/graveler"
                },
                {
                    "number": 76,
                    "name": "golem",
                    "height": 14,
                    "weight": 3000,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/76.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/76.png",
                    "types": [
                        "ground",
                        "rock"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/golem"
                },
                {
                    "number": 77,
                    "name": "ponyta",
                    "height": 10,
                    "weight": 300,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/77.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/77.png",
                    "types": [
                        "fire"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/ponyta"
                },
                {
                    "number": 78,
                    "name": "rapidash",
                    "height": 17,
                    "weight": 950,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/78.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/78.png",
                    "types": [
                        "fire"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/rapidash"
                },
                {
                    "number": 79,
                    "name": "slowpoke",
                    "height": 12,
                    "weight": 360,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/79.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/79.png",
                    "types": [
                        "psychic",
                        "water"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/slowpoke"
                },
                {
                    "number": 80,
                    "name": "slowbro",
                    "height": 16,
                    "weight": 785,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/80.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/80.png",
                    "types": [
                        "psychic",
                        "water"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/slowbro"
                },
                {
                    "number": 81,
                    "name": "magnemite",
                    "height": 3,
                    "weight": 60,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/81.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/81.png",
                    "types": [
                        "steel",
                        "electric"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/magnemite"
                },
                {
                    "number": 82,
                    "name": "magneton",
                    "height": 10,
                    "weight": 600,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/82.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/82.png",
                    "types": [
                        "steel",
                        "electric"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/magneton"
                },
                {
                    "number": 83,
                    "name": "farfetchd",
                    "height": 8,
                    "weight": 150,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/83.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/83.png",
                    "types": [
                        "flying",
                        "normal"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/farfetchd"
                },
                {
                    "number": 84,
                    "name": "doduo",
                    "height": 14,
                    "weight": 392,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/84.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/84.png",
                    "types": [
                        "flying",
                        "normal"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/doduo"
                },
                {
                    "number": 85,
                    "name": "dodrio",
                    "height": 18,
                    "weight": 852,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/85.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/85.png",
                    "types": [
                        "flying",
                        "normal"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/dodrio"
                },
                {
                    "number": 86,
                    "name": "seel",
                    "height": 11,
                    "weight": 900,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/86.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/86.png",
                    "types": [
                        "water"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/seel"
                },
                {
                    "number": 87,
                    "name": "dewgong",
                    "height": 17,
                    "weight": 1200,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/87.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/87.png",
                    "types": [
                        "ice",
                        "water"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/dewgong"
                },
                {
                    "number": 88,
                    "name": "grimer",
                    "height": 9,
                    "weight": 300,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/88.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/88.png",
                    "types": [
                        "poison"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/grimer"
                },
                {
                    "number": 89,
                    "name": "muk",
                    "height": 12,
                    "weight": 300,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/89.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/89.png",
                    "types": [
                        "poison"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/muk"
                },
                {
                    "number": 90,
                    "name": "shellder",
                    "height": 3,
                    "weight": 40,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/90.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/90.png",
                    "types": [
                        "water"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/shellder"
                },
                {
                    "number": 91,
                    "name": "cloyster",
                    "height": 15,
                    "weight": 1325,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/91.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/91.png",
                    "types": [
                        "ice",
                        "water"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/cloyster"
                },
                {
                    "number": 92,
                    "name": "gastly",
                    "height": 13,
                    "weight": 1,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/92.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/92.png",
                    "types": [
                        "poison",
                        "ghost"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/gastly"
                },
                {
                    "number": 93,
                    "name": "haunter",
                    "height": 16,
                    "weight": 1,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/93.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/93.png",
                    "types": [
                        "poison",
                        "ghost"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/haunter"
                },
                {
                    "number": 94,
                    "name": "gengar",
                    "height": 15,
                    "weight": 405,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/94.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/94.png",
                    "types": [
                        "poison",
                        "ghost"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/gengar"
                },
                {
                    "number": 95,
                    "name": "onix",
                    "height": 88,
                    "weight": 2100,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/95.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/95.png",
                    "types": [
                        "ground",
                        "rock"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/onix"
                },
                {
                    "number": 96,
                    "name": "drowzee",
                    "height": 10,
                    "weight": 324,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/96.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/96.png",
                    "types": [
                        "psychic"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/drowzee"
                },
                {
                    "number": 97,
                    "name": "hypno",
                    "height": 16,
                    "weight": 756,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/97.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/97.png",
                    "types": [
                        "psychic"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/hypno"
                },
                {
                    "number": 98,
                    "name": "krabby",
                    "height": 4,
                    "weight": 65,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/98.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/98.png",
                    "types": [
                        "water"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/krabby"
                },
                {
                    "number": 99,
                    "name": "kingler",
                    "height": 13,
                    "weight": 600,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/99.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/99.png",
                    "types": [
                        "water"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/kingler"
                },
                {
                    "number": 100,
                    "name": "voltorb",
                    "height": 5,
                    "weight": 104,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/100.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/100.png",
                    "types": [
                        "electric"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/voltorb"
                },
                {
                    "number": 101,
                    "name": "electrode",
                    "height": 12,
                    "weight": 666,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/101.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/101.png",
                    "types": [
                        "electric"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/electrode"
                },
                {
                    "number": 102,
                    "name": "exeggcute",
                    "height": 4,
                    "weight": 25,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/102.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/102.png",
                    "types": [
                        "psychic",
                        "grass"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/exeggcute"
                },
                {
                    "number": 103,
                    "name": "exeggutor",
                    "height": 20,
                    "weight": 1200,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/103.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/103.png",
                    "types": [
                        "psychic",
                        "grass"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/exeggutor"
                },
                {
                    "number": 104,
                    "name": "cubone",
                    "height": 4,
                    "weight": 65,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/104.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/104.png",
                    "types": [
                        "ground"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/cubone"
                },
                {
                    "number": 105,
                    "name": "marowak",
                    "height": 10,
                    "weight": 450,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/105.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/105.png",
                    "types": [
                        "ground"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/marowak"
                },
                {
                    "number": 106,
                    "name": "hitmonlee",
                    "height": 15,
                    "weight": 498,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/106.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/106.png",
                    "types": [
                        "fighting"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/hitmonlee"
                },
                {
                    "number": 107,
                    "name": "hitmonchan",
                    "height": 14,
                    "weight": 502,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/107.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/107.png",
                    "types": [
                        "fighting"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/hitmonchan"
                },
                {
                    "number": 108,
                    "name": "lickitung",
                    "height": 12,
                    "weight": 655,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/108.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/108.png",
                    "types": [
                        "normal"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/lickitung"
                },
                {
                    "number": 109,
                    "name": "koffing",
                    "height": 6,
                    "weight": 10,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/109.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/109.png",
                    "types": [
                        "poison"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/koffing"
                },
                {
                    "number": 110,
                    "name": "weezing",
                    "height": 12,
                    "weight": 95,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/110.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/110.png",
                    "types": [
                        "poison"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/weezing"
                },
                {
                    "number": 111,
                    "name": "rhyhorn",
                    "height": 10,
                    "weight": 1150,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/111.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/111.png",
                    "types": [
                        "rock",
                        "ground"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/rhyhorn"
                },
                {
                    "number": 112,
                    "name": "rhydon",
                    "height": 19,
                    "weight": 1200,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/112.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/112.png",
                    "types": [
                        "rock",
                        "ground"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/rhydon"
                },
                {
                    "number": 113,
                    "name": "chansey",
                    "height": 11,
                    "weight": 346,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/113.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/113.png",
                    "types": [
                        "normal"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/chansey"
                },
                {
                    "number": 114,
                    "name": "tangela",
                    "height": 10,
                    "weight": 350,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/114.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/114.png",
                    "types": [
                        "grass"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/tangela"
                },
                {
                    "number": 115,
                    "name": "kangaskhan",
                    "height": 22,
                    "weight": 800,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/115.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/115.png",
                    "types": [
                        "normal"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/kangaskhan"
                },
                {
                    "number": 116,
                    "name": "horsea",
                    "height": 4,
                    "weight": 80,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/116.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/116.png",
                    "types": [
                        "water"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/horsea"
                },
                {
                    "number": 117,
                    "name": "seadra",
                    "height": 12,
                    "weight": 250,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/117.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/117.png",
                    "types": [
                        "water"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/seadra"
                },
                {
                    "number": 118,
                    "name": "goldeen",
                    "height": 6,
                    "weight": 150,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/118.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/118.png",
                    "types": [
                        "water"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/goldeen"
                },
                {
                    "number": 119,
                    "name": "seaking",
                    "height": 13,
                    "weight": 390,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/119.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/119.png",
                    "types": [
                        "water"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/seaking"
                },
                {
                    "number": 120,
                    "name": "staryu",
                    "height": 8,
                    "weight": 345,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/120.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/120.png",
                    "types": [
                        "water"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/staryu"
                },
                {
                    "number": 121,
                    "name": "starmie",
                    "height": 11,
                    "weight": 800,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/121.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/121.png",
                    "types": [
                        "psychic",
                        "water"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/starmie"
                },
                {
                    "number": 122,
                    "name": "mr-mime",
                    "height": 13,
                    "weight": 545,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/122.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/122.png",
                    "types": [
                        "fairy",
                        "psychic"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/mr-mime"
                },
                {
                    "number": 123,
                    "name": "scyther",
                    "height": 15,
                    "weight": 560,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/123.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/123.png",
                    "types": [
                        "flying",
                        "bug"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/scyther"
                },
                {
                    "number": 124,
                    "name": "jynx",
                    "height": 14,
                    "weight": 406,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/124.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/124.png",
                    "types": [
                        "psychic",
                        "ice"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/jynx"
                },
                {
                    "number": 125,
                    "name": "electabuzz",
                    "height": 11,
                    "weight": 300,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/125.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/125.png",
                    "types": [
                        "electric"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/electabuzz"
                },
                {
                    "number": 126,
                    "name": "magmar",
                    "height": 13,
                    "weight": 445,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/126.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/126.png",
                    "types": [
                        "fire"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/magmar"
                },
                {
                    "number": 127,
                    "name": "pinsir",
                    "height": 15,
                    "weight": 550,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/127.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/127.png",
                    "types": [
                        "bug"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/pinsir"
                },
                {
                    "number": 128,
                    "name": "tauros",
                    "height": 14,
                    "weight": 884,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/128.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/128.png",
                    "types": [
                        "normal"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/tauros"
                },
                {
                    "number": 129,
                    "name": "magikarp",
                    "height": 9,
                    "weight": 100,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/129.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/129.png",
                    "types": [
                        "water"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/magikarp"
                },
                {
                    "number": 130,
                    "name": "gyarados",
                    "height": 65,
                    "weight": 2350,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/130.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/130.png",
                    "types": [
                        "flying",
                        "water"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/gyarados"
                },
                {
                    "number": 131,
                    "name": "lapras",
                    "height": 25,
                    "weight": 2200,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/131.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/131.png",
                    "types": [
                        "ice",
                        "water"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/lapras"
                },
                {
                    "number": 132,
                    "name": "ditto",
                    "height": 3,
                    "weight": 40,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/132.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/132.png",
                    "types": [
                        "normal"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/ditto"
                },
                {
                    "number": 133,
                    "name": "eevee",
                    "height": 3,
                    "weight": 65,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/133.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/133.png",
                    "types": [
                        "normal"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/eevee"
                },
                {
                    "number": 134,
                    "name": "vaporeon",
                    "height": 10,
                    "weight": 290,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/134.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/134.png",
                    "types": [
                        "water"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/vaporeon"
                },
                {
                    "number": 135,
                    "name": "jolteon",
                    "height": 8,
                    "weight": 245,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/135.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/135.png",
                    "types": [
                        "electric"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/jolteon"
                },
                {
                    "number": 136,
                    "name": "flareon",
                    "height": 9,
                    "weight": 250,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/136.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/136.png",
                    "types": [
                        "fire"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/flareon"
                },
                {
                    "number": 137,
                    "name": "porygon",
                    "height": 8,
                    "weight": 365,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/137.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/137.png",
                    "types": [
                        "normal"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/porygon"
                },
                {
                    "number": 138,
                    "name": "omanyte",
                    "height": 4,
                    "weight": 75,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/138.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/138.png",
                    "types": [
                        "water",
                        "rock"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/omanyte"
                },
                {
                    "number": 139,
                    "name": "omastar",
                    "height": 10,
                    "weight": 350,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/139.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/139.png",
                    "types": [
                        "water",
                        "rock"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/omastar"
                },
                {
                    "number": 140,
                    "name": "kabuto",
                    "height": 5,
                    "weight": 115,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/140.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/140.png",
                    "types": [
                        "water",
                        "rock"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/kabuto"
                },
                {
                    "number": 141,
                    "name": "kabutops",
                    "height": 13,
                    "weight": 405,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/141.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/141.png",
                    "types": [
                        "water",
                        "rock"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/kabutops"
                },
                {
                    "number": 142,
                    "name": "aerodactyl",
                    "height": 18,
                    "weight": 590,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/142.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/142.png",
                    "types": [
                        "flying",
                        "rock"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/aerodactyl"
                },
                {
                    "number": 143,
                    "name": "snorlax",
                    "height": 21,
                    "weight": 4600,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/143.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/143.png",
                    "types": [
                        "normal"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/snorlax"
                },
                {
                    "number": 144,
                    "name": "articuno",
                    "height": 17,
                    "weight": 554,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/144.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/144.png",
                    "types": [
                        "flying",
                        "ice"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/articuno"
                },
                {
                    "number": 145,
                    "name": "zapdos",
                    "height": 16,
                    "weight": 526,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/145.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/145.png",
                    "types": [
                        "flying",
                        "electric"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/zapdos"
                },
                {
                    "number": 146,
                    "name": "moltres",
                    "height": 20,
                    "weight": 600,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/146.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/146.png",
                    "types": [
                        "flying",
                        "fire"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/moltres"
                },
                {
                    "number": 147,
                    "name": "dratini",
                    "height": 18,
                    "weight": 33,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/147.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/147.png",
                    "types": [
                        "dragon"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/dratini"
                },
                {
                    "number": 148,
                    "name": "dragonair",
                    "height": 40,
                    "weight": 165,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/148.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/148.png",
                    "types": [
                        "dragon"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/dragonair"
                },
                {
                    "number": 149,
                    "name": "dragonite",
                    "height": 22,
                    "weight": 2100,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/149.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/149.png",
                    "types": [
                        "flying",
                        "dragon"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/dragonite"
                },
                {
                    "number": 150,
                    "name": "mewtwo",
                    "height": 20,
                    "weight": 1220,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/150.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/150.png",
                    "types": [
                        "psychic"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/mewtwo"
                },
                {
                    "number": 151,
                    "name": "mew",
                    "height": 4,
                    "weight": 40,
                    "image_front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/151.png",
                    "image_back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/151.png",
                    "types": [
                        "psychic"
                    ],
                    "url": "https://pokemon.fandom.com/wiki/mew"
                }
        ]
    }
});
