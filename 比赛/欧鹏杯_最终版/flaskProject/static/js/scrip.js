// 右侧边栏
document.addEventListener('DOMContentLoaded', () => {
  const toggleButton = document.getElementById('toggle');
  const infoPanel = document.querySelector('aside');

  toggleButton.addEventListener('click', () => {
    if (infoPanel.style.right === '0px') {
      infoPanel.style.right = '-370px';
    } else {
      infoPanel.style.right = '0px';
    }
  });
});

// 轮播
const imgData = [
  { url: '/images/动漫大图1.png', title: '热点小故事：红丝带背后的无私关爱——王克荣医生', txt: '王克荣，北京地坛医院感染中心的护士长，同时担任北京红丝带之家办公室主任，致力于艾滋病患者的护理与支持。自1997年接触第一位艾滋病患者起，王克荣的生活与工作重心便转向了对这一群体的帮助。她不仅在医院内提供专业护理，更走出医院，深入河南等地的艾滋病高发区，进行防治知识的普及和志愿者队伍的建设。在过去的十几年里，王克荣积极参与艾滋病患者的心理危机干预，面对患者的绝望和无助，她总是第一时间提供帮助。例如，2006年她通过短信和电话，阻止了一名即将结婚的年轻人自杀的行为。她的行动不仅限于个别案例，王克荣还通过设立医疗点、进行公众演讲和培训，扩大了她的影响力。2002年，王克荣帮助建立了地坛医院“红丝带之家”在河南的医疗点，为当地艾滋病患者提供了长期的医疗援助和教育。她在全国范围内积极培训医务人员，从艾滋病的基本医疗护理到心理咨询，都有所涉猎。王克荣的工作和热情获得了国内外的认可，她是中国唯一一位荣获英国贝利・马丁奖的护士。她的手机中存储着700多个艾滋病患者的联系方式，她常说：“只要病人需要，我随时接听回复。”这种无私的奉献精神和对患者深刻的理解与关怀，使她在艾滋病防治领域里成为了一位不可多得的英雄。' },
  { url: '/images/动漫大图2.png', title: '热点小故事：受到歧视只能憋在心里——艾滋病患儿胡泽涛', txt: '胡泽涛，1998年生，山西临汾市传染病医院红丝带小学4年级学生，因母婴传播感染艾滋病毒。谈到妈妈，12岁的他说印象已经模糊了。他依然记得的是，生他的时候，妈妈剖腹产失血过多需要输血，此时他仍未降生，结果“输上坏人的血了”，妈妈和他都感染了艾滋病。4岁的时候，妈妈走了。7岁的时候，他也被查出患上了艾滋病。跟许多家庭一样，他爸爸没有放弃，虽然当时大哭了一场，但接着到处求医。他没有说及家里的颠沛流离，只说到红丝带小学5年，这里就是他的家。老家离他很遥远，虽然每到放假他仍旧回去。小伙伴不跟他玩，他在老家的小学一出现，孩子们就捂着嘴跑开，用他的话说，看到这样的场景“他只能憋着”。他只是临汾市传染病医院红丝带小学16名艾滋病患儿中的普通一人，直到被顾长卫选中主演一部预计9月上映的反歧视电影，他才成为这所学校的“名人”。他的梦想是：以后所有的人都不生这个病;学校所有的孩子都能够上大学。他不知道的是：因为随时可能发病严重，他们中的大多数人也许都等不到上大学的那个年龄到来。临汾市传染病医院和几名专注于艾滋病救助的NGO组织工作人员说，在山西、四川、广西、云南和河南，像这样的孩子还有很多，他们大都因母婴传播染病。能像这16名孩子有较好的受教育和治疗条件的，几乎没有。' }
]

const img = document.querySelector('.today .main img')
const p1 = document.querySelector('.today .main .bottom p')
const p2 = document.querySelector('.today .footer p')

//1.右侧按钮业务
let i = 0
//1.1 获取右侧按钮
const next = document.querySelector('.today .next')
//1.2 注册点击事件
next.addEventListener('click', () => {
  i++
  //大于8
  if (i >= imgData.length) {
    i = 0
  }
  renderImg()
})

//2.左侧按钮业务
//2.1 获取左侧按钮
const prev = document.querySelector('.today .prev')

//2.2 注册点击事件
prev.addEventListener('click', () => {
  i--
  //小于0
  if (i < 0) {
    i = imgData.length - 1
  }
  renderImg()
})

//抽取渲染函数作为复用
function renderImg() {
  img.src = imgData[i].url
  p1.innerHTML = imgData[i].title
  p2.innerHTML = imgData[i].txt
}

//3.自动播放模块
let imgTime = setInterval(() => {
  //利用js自动调用点击事件 click()
  next.click()
}, 3000)

//4.鼠标进入大盒子，停止定时器
//注册事件
const slider = document.querySelector('.today')
slider.addEventListener('mouseenter', () => {
  clearInterval(imgTime)
})

//5.鼠标离开大盒子，开启定时器 先停止再开启
slider.addEventListener('mouseleave', () => {
  clearInterval(imgTime)
  imgTime = setInterval(() => {
    //利用js自动调用点击事件 click()
    next.click()
  }, 3000)
})
