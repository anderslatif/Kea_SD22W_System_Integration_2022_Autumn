import express from "express";
const app = express();

app.use(express.urlencoded({ extended: true }));

import cors from "cors";
app.use(cors());

import multer from "multer";
const storage = multer.diskStorage({
    destination: (req, file, cb) => {
        cb(null, "./uploads");
    },
    filename: (req, file, cb) => {
        const dateString = new Date().toISOString();
        cb(null, `${dateString}____${file.originalname}`);
    }
})
const upload = multer({ storage: storage });


app.post("/basicform", (req, res) => {
    console.log(req.body);
    res.send({ message: "OK" });
});

app.post("/fileupload", upload.single('file'),  (req, res) => {
    console.log(req.file);
    res.send({ message: "OK" });
});

const PORT = 8000;
app.listen(PORT, (req, res) => console.log("Server running on port", PORT));