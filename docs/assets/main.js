// boxkit landing — живой терминал в хиро-блоке
(function () {
  "use strict";

  var el = document.getElementById("terminal");
  if (!el) return;

  var lines = [
    { text: "$ python boxkit/genpass.py --length 24", cls: "" },
    { text: "Rm#8vTq2wLpZx94Kd7JfNc3b", cls: "t-output" },
    { text: "$ python boxkit/organizer.py ~/Downloads", cls: "" },
    { text: "photo.jpg   -> images/photo.jpg", cls: "t-output" },
    { text: "report.pdf  -> documents/report.pdf", cls: "t-output" },
    { text: "song.mp3    -> audio/song.mp3", cls: "t-output" },
    { text: "$ _", cls: "t-cursor" }
  ];

  var pre = el.querySelector("code");
  var lineIndex = 0;
  var charIndex = 0;
  var current = null;

  pre.innerHTML = "";

  // Упрощённый тайпрайтер: каждая строка — один span, у prompt-строк
  // зелёный "$", у флагов синий акцент.
  function type() {
    if (lineIndex >= lines.length) {
      setTimeout(function () {
        pre.innerHTML = "";
        lineIndex = 0;
        charIndex = 0;
        type();
      }, 5000);
      return;
    }
    var item = lines[lineIndex];
    if (charIndex === 0) {
      current = document.createElement("span");
      current.className = item.cls;
      pre.appendChild(current);
    }
    var text = item.text;
    if (text.charAt(0) === "$") {
      // Показываем команду целиком с подсветкой prompt и флагов
      var flagIdx = text.indexOf("--");
      var html = '<span class="t-prompt">$</span> ';
      var rest = text.slice(2);
      if (flagIdx > 0) {
        html += rest.slice(0, flagIdx - 2) + '<span class="t-flag">' + rest.slice(flagIdx - 2) + "</span>";
      } else {
        html += rest;
      }
      current.innerHTML = html;
      lineIndex++;
      charIndex = 0;
      setTimeout(type, 450);
      return;
    }
    current.textContent = text.slice(0, charIndex + 1);
    charIndex++;
    if (charIndex >= text.length) {
      lineIndex++;
      charIndex = 0;
      setTimeout(type, 350);
      return;
    }
    setTimeout(type, 40 + Math.random() * 50);
  }

  type();
})();
