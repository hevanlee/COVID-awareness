const functions = require('firebase-functions');
const admin = require('firebase-admin');

admin.initializeApp();

const express = require('express');
const app = express();
//const cors = require('cors');
//app.use(cors({origin: true}));

const db = admin.firestore();


/* app.get("/hi", (request, response) => {
    response.send("Hello world!");
});  */
app.use('/test', function (req,res) {
    //res.render('EJS/test')
    response.send("Hello world!");
});




exports.app = functions.https.onRequest(app);

// // Create and Deploy Your First Cloud Functions
// // https://firebase.google.com/docs/functions/write-firebase-functions
//
// exports.helloWorld = functions.https.onRequest((request, response) => {
//   functions.logger.info("Hello logs!", {structuredData: true});
//   response.send("Hello from Firebase!");
// });
