const express = require('express');

const path = require('path');
let {PythonShell} = require('python-shell')
const app = new express();
app.use(express.static("machine_learning"))
app.use(express.json())
app.use(express.urlencoded())
const ejs = require('ejs');
app.set('view engine', 'ejs');

app.listen(4000, () => {
    console.log('App listening on port 4000');
});
app.get('/',async (req,res) =>{
    res.render('home');
})
app.post('/submit',async (req,res) =>{    
    let params=req.body["symptoms"]
    let options={
        mode:'text',
        pythonOptions:['-u'],
        args:params
    };
    PythonShell.run('prediction.py',options).then(messages=>{
        res.send(messages)
    });

})