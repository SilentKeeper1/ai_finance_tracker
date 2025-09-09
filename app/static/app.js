document.addEventListener('DOMContentLoaded', ()=>{
// Dashboard chart
const expenseChartEl = document.getElementById('expenseChart');
if(expenseChartEl){
const ctx = expenseChartEl.getContext('2d');
new Chart(ctx, {
type:'bar',
data:{labels:['Food','Transport','Entertainment','Other'], datasets:[{label:'Expenses', data:[120,80,50,30], backgroundColor:'rgba(110,231,183,0.7)'}]},
options:{responsive:true,plugins:{legend:{display:false}}}
});
}


// AI Chat
const chatBox = document.getElementById('chatBox');
const chatInput = document.getElementById('chatInput');
const sendBtn = document.getElementById('sendBtn');
if(sendBtn){
sendBtn.addEventListener('click', async ()=>{
const msg = chatInput.value.trim();
if(!msg) return;
const div = document.createElement('div');
div.textContent = 'You: '+msg;
div.className='mb-2';
chatBox.appendChild(div);
chatInput.value='';
//