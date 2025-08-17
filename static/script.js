// كود لتوسيع الـ textarea تلقائيًا
const input = document.getElementById("user-input");

input.addEventListener("input", () => {
  input.style.height = "auto"; // إعادة تعيين الارتفاع
  input.style.height = input.scrollHeight + "px"; // تعيين الارتفاع حسب المحتوى
});

async function sendMessage() {
  const chatBox = document.getElementById("chat-box");
  const message = input.value.trim();

  if (!message) return;

  // عرض رسالة المستخدم
  const userDiv = document.createElement("div");
  userDiv.classList.add("message", "user");
  userDiv.innerText = message;
  chatBox.appendChild(userDiv);

  input.value = "";
  input.style.height = "40px"; // إعادة ارتفاع الصندوق للابتدائي بعد الإرسال

  // إرسال الرسالة للسيرفر
  const response = await fetch("/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message })
  });

  const data = await response.json();

  // عرض رد البوت
  const botDiv = document.createElement("div");
  botDiv.classList.add("message", "bot");
  botDiv.innerText = data.reply;
  chatBox.appendChild(botDiv);

  chatBox.scrollTop = chatBox.scrollHeight;
}