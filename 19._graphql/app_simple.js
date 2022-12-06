import express from "express";
const app = express();
app.use(express.static("public"));

import { GraphQLObjectType, GraphQLSchema, GraphQLString } from "graphql";

const schema = new GraphQLSchema({
    query: new GraphQLObjectType({
        name: "RootQueryType",
        fields: {
            hello: {
                type: GraphQLString,
                resolve: () => "world"
            }
        }
    })
});


import { graphqlHTTP } from "express-graphql";
app.use("/graphql", graphqlHTTP({
    schema,
    graphiql: true
}));



const PORT = process.env.PORT || 8080;
app.listen(PORT, () => console.log("Server is running on port", PORT));
