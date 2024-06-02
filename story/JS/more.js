// 动态加载
// 在文档加载完成后执行函数
document.addEventListener('DOMContentLoaded', function () {
  loadData('/api/heros', 'heroContainer', 'img');   // 加载并展示英雄数据
  loadData('/api/storys', 'storyContainer', 'img'); // 加载并展示故事数据
  loadData('/api/videos', 'videoContainer', 'video', true); // 加载并展示视频数据，包含分割线
});

/**
 * 加载数据并展示到指定容器
 * 
 * @param {string} apiEndpoint API端点
 * @param {string} containerId 容器的ID
 * @param {string} mediaType 媒体类型 ('img' 或 'video')
 * @param {boolean} includeHr 
 */
function loadData(apiEndpoint, containerId, mediaType, includeHr = false) {
  fetch(apiEndpoint)
    .then(response => response.json())
    .then(data => {
      // 获取元素
      const container = document.getElementById(containerId);
      // 遍历
      data.forEach(item => {
        // 创建元素
        const section = document.createElement('div');
        section.className = 'section';
        let mediaContent;

        // 选择正确的URL字段
        const url = mediaType === 'img' ? (item.heroUrl || item.storyUrl) : item.videoUrl;

        // 判断媒体类型决定如何渲染
        if (mediaType === 'img') {
          mediaContent = `<img src="${url}" alt="Image">`;
        } else if (mediaType === 'video') {
          mediaContent = `<video src="${url}" controls></video>`;
        }

        // 设置内部HTML
        if (mediaType === 'img') {
          section.innerHTML = `
          <h2>${item.title}</h2>
          <p>${item.description}<a href="${item.detail}">查看完整故事>></a></p>
          ${mediaContent}
        `;
        } else {
          section.innerHTML = `
          <h2>${item.title}</h2>
          <p>${item.description}</p>
          ${mediaContent}
        `;
        }


        // 是否包含水平分割线 (可选)
        container.appendChild(section);
        if (includeHr) {
          const hr = document.createElement('hr');
          container.appendChild(hr);
        }
      });
    })
}
