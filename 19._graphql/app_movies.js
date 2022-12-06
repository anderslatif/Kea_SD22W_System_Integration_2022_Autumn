import express from "express";
const app = express();

let movieId = 4;
const movies = [
    { id: 1, title: "The Unbearable Weight of Massive Talent", actorIds: [1] },
    { id: 2, title: "Pig", actorIds: [1] },
    { id: 3, title: "One Flew Over the Cuckoo's Nest", actorIds: [2] },
    { id: 4, title: "Junior", actorIds: [2, 3] },
];
 
let actorId = 3;
const actors = [
    { id: 1, name: "Nicolas Cage" },
    { id: 2, name: "Danny DeVito" },
    { id: 3, name: "Arnold Schwarzenegger" },
];

import { GraphQLSchema, GraphQLObjectType, GraphQLInt, GraphQLString, GraphQLList } from "graphql";

const ActorType = new GraphQLObjectType({
    name: "Actor",
    description: "An actor",
    fields: () => ({
        id: { type: GraphQLInt },
        name: { type: GraphQLString },
        movies: { 
            type: new GraphQLList(MovieType),
            resolve: (actor) => {
                return movies.filter(movie => movie.actorIds.includes(actor.id));
            }
        }
    })
});

const MovieType = new GraphQLObjectType({
    name: "Movie",
    description: "A movie",
    fields: {
        id: { type: GraphQLInt },
        title: { type: GraphQLString },
        actorIds: { type: new GraphQLList(GraphQLInt) },
        actors: {
            type: new GraphQLList(ActorType),
            description: "Get all the actors that belong to a movie",
            resolve: (movie) => {
                return movie.actorIds.map(actorId => actors.find(actor => actor.id === actorId));
            }
        }
    }
});

const RootQueryType = new GraphQLObjectType({
        name: "RootQueryType",
        fields: {
            movies: {
                type: new GraphQLList(MovieType),
                description: "All movies",
                resolve: () => movies
            },
            actors: {
                type: new GraphQLList(ActorType),
                description: "All actors",
                resolve: () => actors
            }
        }
});

const schema = new GraphQLSchema({
    query: RootQueryType
});

import { graphqlHTTP } from "express-graphql";
app.use("/graphql", graphqlHTTP({
    schema,
    graphiql: true
}));


const PORT = process.env.PORT || 8080;
app.listen(PORT, () => console.log("Server is running on port", PORT));
