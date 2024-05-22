<!DOCTYPE html>
<html>
<head>
    <title>RihardsiBigdejs</title>
</head>
<body>
    <canvas id="Canvas" width="1200" height="900" style="background-size: cover; background:url(https://live.staticflickr.com/4113/5611588305_53ec341dbf_b.jpg)"></canvas>
    <script>
        var score = 0;
        var FPS = 40;
        var cva = Canvas.getContext("2d");
        var game_end = false;
        var Timeout1;
        var Timeout2;
        var Skibidi = new MainPlayer("https://npr.brightspotcdn.com/dims4/default/2feadaf/2147483647/strip/true/crop/3594x2478+0+0/resize/880x607!/quality/90/?url=http%3A%2F%2Fnpr-brightspot.s3.amazonaws.com%2Fa1%2F92%2F0591e3bf4effb61e2eab9206a4e7%2Fbmw2.jpg");
        var Sigma = [];
        var Rizz = [];
        var remainingTime = 180;
        var speed = 6
        var initialSpeed = {
            Rizz: { x: (Math.random() * 1) + 0.5, y: (Math.random() * 1.5) + 0.5 },
            Sigma: { x: (Math.random() * 1) + 0.5, y: (Math.random() * 1.5) + 0.5 }
        };

        function MainPlayer(img_url) {
            this.x = 0;
            this.y = 0;
            this.visible = true;
            this.velocity_x = 0;
            this.velocity_y = 0;
            this.MyImg = new Image();
            this.MyImg.src = img_url;
        }

        MainPlayer.prototype.Random = function () {
            this.x = Math.random() * (Canvas.width - this.MyImg.width);
        }

        MainPlayer.prototype.Frame = function () {
            if (this.visible) cva.drawImage(this.MyImg, this.x, this.y);
            if ((this.velocity_x < 0) && (this.x > 0)) this.x = this.x + this.velocity_x;
            if ((this.velocity_x > 0) && (this.x + this.MyImg.width < Canvas.width)) this.x = this.x + this.velocity_x;
            if ((this.velocity_y < 0) && (this.y > 0)) this.y = this.y + this.velocity_y;
            if ((this.velocity_y > 0) && (this.y + this.MyImg.height < Canvas.height)) this.y = this.y + this.velocity_y;
        }

        MainPlayer.prototype.Frame = function() {
            if ((this.velocity_x < 0) && (this.x > 0))  this.x = this.x + this.velocity_x;
            if ((this.velocity_x > 0) && (this.x + this.MyImg.width < Canvas.width )) this.x = this.x + this.velocity_x;
            if ((this.velocity_y < 0) && (this.y > 0))  this.y = this.y + this.velocity_y;
            if ((this.velocity_y > 0) && (this.y + this.MyImg.height< Canvas.height)) this.y = this.y + this.velocity_y;
        }       


        function ImgTouch(thing1, thing2) {
            if (!thing1.visible || !thing2.visible) return false;
            if (thing1.x >= thing2.x + thing2.MyImg.width || thing1.x + thing1.MyImg.width <= thing2.x) return false;
            if (thing1.y >= thing2.y + thing2.MyImg.height || thing1.y + thing1.MyImg.height <= thing2.y) return false;
            return true;
        }

        function SigmasTouchingSkibidi(Sigmas, Skibidi) {
            return (
                Skibidi.x < Sigmas.x + Sigmas.MyImg.width &&
                Skibidi.x + Skibidi.MyImg.width > Sigmas.x &&
                Skibidi.y < Sigmas.y + Sigmas.MyImg.height &&
                Skibidi.y + Skibidi.MyImg.height > Sigmas.y
            );
        }

        function KeyUp(MyEvent) {
            if (MyEvent.keyCode == 37) { Skibidi.velocity_x = 0 };
            if (MyEvent.keyCode == 38) { Skibidi.velocity_y = 0 };
            if (MyEvent.keyCode == 39) { Skibidi.velocity_x = 0 };
            if (MyEvent.keyCode == 40) { Skibidi.velocity_y = 0 };
        }

        function KeyDown(MyEvent) {
            if (MyEvent.keyCode == 37) { Skibidi.velocity_x = -speed };
            if (MyEvent.keyCode == 38) { Skibidi.velocity_y = -speed };
            if (MyEvent.keyCode == 39) { Skibidi.velocity_x = speed };
            if (MyEvent.keyCode == 40) { Skibidi.velocity_y = speed };
            if (MyEvent.keyCode == 83 && game_end) game_restart();
            MyEvent.preventDefault()
        }

        function AddRizzes() {
            var noRizz = new MainPlayer("https://static1.topspeedimages.com/wordpress/wp-content/uploads/2023/08/three-quarter-view-of-ferrari-812-superfast.jpghttps://i.ytimg.com/vi/iZt7Fwu91FI/maxresdefault.jpg");
            if (Math.random() < 0.5) {
                noRizz.velocity_y = initialSpeed.Rizz.y;
                noRizz.velocity_x = 0;
            } else {
                noRizz.velocity_y = initialSpeed.Rizz.y;
                noRizz.velocity_x = (Math.random() < 0.5 ? -1 : 1) * initialSpeed.Rizz.x;
            }
            noRizz.Random();
            Rizz.push(noRizz);
            setTimeout(AddRizzes, Math.random() * 5000 / Math.pow(1.1, (Math.log(initialSpeed.Rizz.x) / Math.log(1.1))));
        }

        function AddSigmas() {
            var noSigma = new MainPlayer("https://static1.topspeedimages.com/wordpress/wp-content/uploads/2023/08/three-quarter-view-of-ferrari-812-superfast.jpg");
            if (Math.random() < 0.5) {
                noSigma.velocity_y = initialSpeed.Sigma.y;
                noSigma.velocity_x = 0;
            } else {
                noSigma.velocity_y = initialSpeed.Sigma.y;
                noSigma.velocity_x = (Math.random() < 0.5 ? -1 : 1) * initialSpeed.Sigma.x;
            }
            noSigma.Random();
            Sigma.push(noSigma);
            setTimeout(AddSigmas, Math.random() * 4000 / Math.pow(1.1, (Math.log(initialSpeed.Sigma.x) / Math.log(1.1))));
        }

        function game_restart() {
            score = 0;
            game_end = false;
            remainingTime = 180;
            initialSpeed = {
                Rizz: { x: (Math.random() * 1) + 0.5, y: (Math.random() * 1) + 0.5 },
                Sigma: { x: (Math.random() * 1) + 0.5, y: (Math.random() * 1) + 0.5 }
            };
            Rizz = [];
            Sigma = [];
            clearTimeout(Timeout2);
            clearTimeout(Timeout1);
            AddRizzes();
            AddSigmas();
            Skibidi.x = 0;
            Skibidi.y = Canvas.height - Skibidi.MyImg.height;
        }

        function Score_show() {
            cva.fillStyle = "white";
            cva.font = "20px Arial";
            cva.fillText("Punkti: " + score, 15, 20);
        }

        function Timer_show() {
            cva.fillStyle = "white";
            cva.font = "20px Arial";
            cva.fillText("Laiks: " + Math.ceil(remainingTime), Canvas.width - 105, 20);
        }

        function GameOver_show() {
            cva.fillStyle = "red";
            cva.font = "bold 50px Arial";
            cva.textAlign = "center";
            cva.fillText("Game Over", Canvas.width / 2, Canvas.height / 2);
            cva.font = "bold 20px Arial";
            cva.fillText("Press S to play again", Canvas.width / 2, (Canvas.height / 2) + 50);
            cva.textAlign = "left";
        }

        function Do_a_Frame() {
            cva.clearRect(0, 0, Canvas.width, Canvas.height);
            Score_show();
            Timer_show();
            Skibidi.Frame();
            cva.drawImage(Skibidi.MyImg, Skibidi.x, Skibidi.y);
            if (!game_end) {
                remainingTime -= 1 / FPS;
                if (remainingTime <= 0) {
                    game_end = true;
                }

                for (var i = 0; i < Sigma.length; i++) {
                    var Sigmas = Sigma[i];
                    Sigmas.Frame();
                    cva.drawImage(Sigmas.MyImg, Sigmas.x, Sigmas.y);

                    if (SigmasTouchingSkibidi(Sigmas, Skibidi)) {
                        Sigma.splice(i, 1);
                        score += 1;
                    }
                    if (Sigmas.y + Sigmas.MyImg.height > Canvas.height) {
                        Sigma.splice(i, 1);
                        i--;
                        score -= 1;
                    }
                }

                for (var j = 0; j < Rizz.length; j++) {
                    var Rizzes = Rizz[j];
                    Rizzes.Frame();
                    cva.drawImage(Rizzes.MyImg, Rizzes.x, Rizzes.y);

                    if (Rizzes.y + Rizzes.MyImg.height > Canvas.height) {
                        Rizz.splice(j, 1);
                        j--;
                        score++;
                    }
                }

                for (var k = 0; k < Rizz.length; k++) {
                    if (ImgTouch(Skibidi, Rizz[k])) {
                        game_end = true;
                        break;
                    }
                }
            }
            if (game_end) GameOver_show();
        }

        addEventListener("keyup", KeyUp);
        addEventListener("keydown", KeyDown);
        setInterval(Do_a_Frame, 1000 / FPS);
        game_restart();
    </script>
</body>
</html>
