<script>
            $(function() {
                thing();
            });
            function thing() {
            function a(a, b, c, d, e) {
                this.beginX = a, this.beginY = b, this.closeX = c, this.closeY = d, this.o = e
            }
            function b(a, b, c, d, e) {
                this.x = a, this.y = b, this.r = c, this.moveX = d, this.moveY = e
            }
            function c(a, b) {
                var c = arguments[1] || 0;
                return Math.floor(Math.random() * (a - c + 1) + c)
            }
            function d(a, c, d, e, f, g) {
                var h = new b(c, d, e, f, g);
                return a.beginPath(), a.arc(h.x, h.y, h.r, 0, 2 * Math.PI), a.closePath(), a.fill(), h
            }
            function e(b, c, d, e, f, g) {
                var h = new a(c, d, e, f, g);
                b.beginPath(), b.strokeStyle = "rgba(255,255,255," + g + ")", b.moveTo(h.beginX, h.beginY), b.lineTo(h.closeX, h.closeY), b.closePath(), b.stroke()
            }
            function f() {
                m = [];
                for (var a = 0; a < j; a++)
                    m.push(d(l, c(h), c(i), c(2, 2), c(10, -10) / 40, c(10, -10) / 40));
                g()
            }
            function g() {
                l.clearRect(0, 0, k.width, k.height);
                for (var a = 0; a < j; a++)
                    d(l, m[a].x, m[a].y, m[a].r);
                for (var a = 0; a < j; a++)
                    for (var b = 0; b < j; b++)
                        if (a + b < j) {
                            var c = Math.abs(m[a + b].x - m[a].x),
                                f = Math.abs(m[a + b].y - m[a].y),
                                g = Math.sqrt(c * c + f * f),
                                h = 1 / g * 7 - .009,
                                i = h > .03 ? .15 : h;
                            i > 0 && e(l, m[a].x, m[a].y, m[a + b].x, m[a + b].y, i)
                        }
            }
            var h = window.innerWidth,
                i = $(".main").height(),
                j = 35,
                k = document.getElementById("my_canvas");
            k.width = h, k.height = i;
            var l = k.getContext("2d");
            l.strokeStyle = "rgba(255,255,255,0.2)", l.strokeWidth = 1, l.fillStyle = "rgba(255,255,255,0.1)";
            var m = [];
            window.onload = function() {
                f(), setInterval(function() {
                    for (var a = 0; a < j; a++) {
                        var b = m[a];
                        b.x += b.moveX, b.y += b.moveY, b.x > h ? b.x = 0 : b.x < 0 && (b.x = h), b.y > i ? b.y = 0 : b.y < 0 && (b.y = i)
                    }
                    g()
                }, 16)
            }
        }
</script>