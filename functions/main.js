const express = require('express')
const router = express.Router()

router.get('/', (req,res) => {

    const data = req.context //{page:.., global:... }
    res.render('landing', data) // Passes data into render
})

module.exports = router