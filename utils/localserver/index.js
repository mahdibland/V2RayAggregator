const express = require("express");
const needle = require("needle");
const { Base64 } = require("js-base64");
// const constant = require("./constant");
const cors = require("cors");

const app = express();
app.use(
  cors({
    origin: "*",
    credentials: true,
  })
);

// app.get("/get-lite-config", async (req, res) => {
//   needle.get(
//     constant.lite_config,
//     {
//       headers: {
//         Authorization: constant.token,
//       },
//     },
//     (err, result, body) => {
//       res.status(200).send(result.body);
//     }
//   );
// });

app.get("/get-base64", async (req, res) => {
  try {
    const { content } = req.query;
    needle.get(
      content,
      {
        timeout: 60000,
      },
      (err, result, body) => {
        if (err) {
          res.status(400).send(err);
          return;
        }
        res.status(200).send(Base64.toBase64(body));
      }
    );
  } catch (error) {
    res.status(400).send(error);
  }
});

let port = process.env.PORT || 3333;
app.listen(port, () => {
  console.log(`successfully running on port ${port}`);
});
