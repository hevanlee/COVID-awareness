const functions = require('firebase-functions');
const admin = require('firebase-admin');
const express = require('express');
const app = express();
//const cors = require('cors');
//app.use(cors({origin: true}));

admin.initializeApp();

const db = admin.firestore();

app.get("/about", (request, response) => {
    //.collection
    //return response.
    functions.logger.info("Hello logs!", {structuredData: true});
    response.send("Hello world!");
});


//exports.api = functions.https.onRequest(app);

// // Create and Deploy Your First Cloud Functions
// // https://firebase.google.com/docs/functions/write-firebase-functions
//
// exports.helloWorld = functions.https.onRequest((request, response) => {
//   functions.logger.info("Hello logs!", {structuredData: true});
//   response.send("Hello from Firebase!");
// });
