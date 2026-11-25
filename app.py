<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>액터스 룸 - 비대면 셀프 테이프 촬영 & 감독 피드백</title>
  <style>
    :root {
      --bg-color: #121212;
      --card-bg: #1e1e1e;
      --accent-color: #e50914;
      --accent-hover: #f40612;
      --success-color: #10b981;
      --warning-color: #f59e0b;
      --text-main: #ffffff;
      --text-sub: #b3b3b3;
      --border-color: #333333;
      --input-bg: #141414;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      font-family: 'Pretendard', -apple-system, BlinkMacSystemFont, system-ui, Roboto, sans-serif;
    }

    body {
      background-color: var(--bg-color);
      color: var(--text-main);
      display: flex;
      justify-content: center;
      min-height: 100vh;
      padding: 20px;
    }

    .app-container {
      width: 100%;
      max-width: 660px;
      background-color: var(--card-bg);
      border-radius: 16px;
      padding: 30px;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
      display: flex;
      flex-direction: column;
      gap: 22px;
    }

    header {
      border-bottom: 1px solid var(--border-color);
      padding-bottom: 16px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    header h1 {
      font-size: 1.4rem;
      font-weight: 700;
      letter-spacing: -0.5px;
    }

    .header-actions {
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .badge {
      background-color: var(--accent-color);
      font-size: 0.75rem;
      padding: 4px 8px;
      border-radius: 4px;
      font-weight: 600;
    }

    .btn-reset {
      background: transparent;
      border: 1px solid #444;
      color: #999;
      font-size: 0.75rem;
      padding: 4px 8px;
      border-radius: 4px;
      cursor: pointer;
    }

    .btn-reset:hover {
      color: white;
      border-color: white;
    }

    .step-section {
      display: none;
      flex-direction: column;
      gap: 16px;
      animation: fadeIn 0.3s ease-in-out;
    }

    .step-section.active {
      display: flex;
    }

    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(10px); }
      to { opacity: 1; transform: translateY(0); }
    }

    .section-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    h2 {
      font-size: 1.15rem;
      color: var(--text-main);
    }

    p.desc {
      font-size: 0.9rem;
      color: var(--text-sub);
      margin-top: -10px;
    }

    .btn-add-toggle {
      background-color: #2c2c2c;
      color: #4ade80;
      border: 1px solid #4ade80;
      padding: 6px 12px;
      border-radius: 6px;
      font-size: 0.85rem;
      font-weight: 600;
      cursor: pointer;
    }

    .add-form {
      display: none;
      flex-direction: column;
      gap: 10px;
      background-color: #252525;
      padding: 16px;
      border-radius: 10px;
      border: 1px solid #444;
    }

    .add-form.open {
      display: flex;
    }

    input[type="text"], input[type="number"], textarea, select {
      width: 100%;
      padding: 12px;
      border-radius: 8px;
      background-color: var(--input-bg);
      color: white;
      border: 1px solid var(--border-color);
      font-size: 0.95rem;
    }

    textarea {
      resize: vertical;
      min-height: 80px;
      line-height: 1.5;
    }

    .grid-list {
      display: grid;
      grid-template-columns: 1fr;
      gap: 12px;
      max-height: 400px;
      overflow-y: auto;
      padding-right: 4px;
    }

    .select-card {
      background-color: #2a2a2a;
      border: 1px solid var(--border-color);
      border-radius: 10px;
      padding: 16px 20px;
      color: var(--text-main);
      text-align: left;
      cursor: pointer;
      transition: all 0.2s;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 12px;
    }

    .select-card:hover {
      background-color: #333333;
      border-color: var(--accent-color);
    }

    .card-content {
      flex: 1;
    }

    .card-title {
      font-size: 1.05rem;
      font-weight: 600;
      line-height: 1.45;
    }

    .card-sub {
      font-size: 0.85rem;
      color: var(--text-sub);
      margin-top: 4px;
    }

    .cutline-badge {
      display: inline-block;
      background-color: rgba(255, 215, 0, 0.15);
      color: #ffd700;
      border: 1px solid rgba(255, 215, 0, 0.4);
      font-size: 0.75rem;
      padding: 2px 8px;
      border-radius: 4px;
      margin-left: 6px;
      font-weight: 600;
    }

    .btn-delete {
      background: transparent;
      border: none;
      color: #777;
      font-size: 1.1rem;
      padding: 4px 8px;
      cursor: pointer;
    }

    .btn-delete:hover {
      color: #ff4d4d;
    }

    .music-box {
      background-color: #252525;
      border-radius: 10px;
      padding: 16px;
      border: 1px dashed #555;
    }

    .music-header {
      margin-bottom: 10px;
      font-size: 0.9rem;
      font-weight: 600;
      color: #ffd700;
    }

    /* 촬영 및 연습 화면 스타일 */
    .practice-stage {
      background-color: #141414;
      border: 1px solid var(--border-color);
      border-radius: 12px;
      padding: 22px 18px;
      text-align: center;
      display: flex;
      flex-direction: column;
      justify-content: center;
      gap: 12px;
    }

    .situation-tag {
      display: inline-block;
      background-color: #2c2c2c;
      color: #ff6b6b;
      padding: 5px 12px;
      border-radius: 20px;
      font-size: 0.85rem;
      margin: 0 auto;
    }

    .script-text {
      font-size: 1.25rem;
      line-height: 1.65;
      font-weight: 500;
      word-break: keep-all;
    }

    .bgm-control-bar {
      background-color: #252525;
      padding: 14px;
      border-radius: 10px;
      border: 1px solid #3d3d3d;
      display: flex;
      flex-direction: column;
      gap: 10px;
    }

    .bgm-status-text {
      font-size: 0.85rem;
      color: #ffd700;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .camera-panel {
      background-color: #222;
      border-radius: 12px;
      padding: 18px;
      border: 1px solid #383838;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 14px;
    }

    .video-wrapper {
      width: 100%;
      background-color: #000;
      border-radius: 10px;
      overflow: hidden;
      position: relative;
      aspect-ratio: 16 / 9;
      display: flex;
      align-items: center;
      justify-content: center;
      border: 1px solid #333;
    }

    video {
      width: 100%;
      height: 100%;
      object-fit: cover;
      background-color: #000;
    }

    /* 셀프 카메라 좌우 반전 */
    #live-camera-preview {
      transform: scaleX(-1);
    }

    .rec-badge-overlay {
      position: absolute;
      top: 12px;
      left: 12px;
      background-color: rgba(0, 0, 0, 0.7);
      padding: 5px 10px;
      border-radius: 6px;
      display: flex;
      align-items: center;
      gap: 6px;
      font-size: 0.8rem;
      font-weight: 700;
      color: white;
    }

    .dot {
      width: 10px;
      height: 10px;
      border-radius: 50%;
      background-color: #666;
    }

    .dot.recording {
      background-color: #ef4444;
      animation: pulse 1s infinite;
    }

    @keyframes pulse {
      0% { transform: scale(1); opacity: 1; }
      50% { transform: scale(1.3); opacity: 0.5; }
      100% { transform: scale(1); opacity: 1; }
    }

    .recognized-box {
      width: 100%;
      background-color: #141414;
      padding: 12px;
      border-radius: 8px;
      font-size: 0.85rem;
      color: #aaa;
      text-align: left;
      border: 1px solid #2e2e2e;
    }

    /* 감독 피드백 화면 스타일 */
    .director-box {
      background-color: #1a1a1a;
      border: 1px solid #444;
      border-radius: 12px;
      padding: 20px;
      display: flex;
      flex-direction: column;
      gap: 14px;
    }

    .score-display {
      text-align: center;
      padding: 16px;
      border-radius: 10px;
      background-color: #121212;
    }

    .score-number {
      font-size: 2.5rem;
      font-weight: 800;
    }

    .score-pass { color: var(--success-color); }
    .score-fail { color: var(--accent-color); }

    .result-banner {
      padding: 14px;
      border-radius: 8px;
      text-align: center;
      font-weight: 700;
      font-size: 1.05rem;
    }

    .banner-pass {
      background-color: rgba(16, 185, 129, 0.15);
      border: 1px solid var(--success-color);
      color: #34d399;
    }

    .banner-fail {
      background-color: rgba(229, 9, 20, 0.15);
      border: 1px solid var(--accent-color);
      color: #f87171;
    }

    .btn-group {
      display: flex;
      gap: 10px;
      width: 100%;
      flex-wrap: wrap;
    }

    button.btn {
      flex: 1;
      min-width: 140px;
      padding: 14px;
      border: none;
      border-radius: 8px;
      font-size: 0.95rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s;
    }

    button.btn:disabled {
      opacity: 0.4;
      cursor: not-allowed;
    }

    .btn-primary {
      background-color: var(--accent-color);
      color: white;
    }

    .btn-primary:hover:not(:disabled) {
      background-color: var(--accent-hover);
    }

    .btn-success {
      background-color: var(--success-color);
      color: #064e3b;
    }

    .btn-secondary {
      background-color: #333;
      color: white;
    }

    .btn-secondary:hover:not(:disabled) {
      background-color: #444;
    }

    audio {
      width: 100%;
      height: 36px;
    }
  </style>
</head>
<body>

<div class="app-container">
  <header>
    <h1>🎬 ACTORS ROOM</h1>
    <div class="header-actions">
      <span class="badge">SELF-TAPE STUDIO</span>
      <button class="btn-reset" onclick="resetData()">초기화</button>
    </div>
  </header>

  <!-- STEP 1: 작품 선택 (drama_name 리스트 기반) -->
  <section id="step-1" class="step-section active">
    <div class="section-header">
      <h2>1. 작품 선택</h2>
      <button class="btn-add-toggle" onclick="toggleForm('work-form')">+ 새 작품 추가</button>
    </div>
    <p class="desc">연습할 작품을 선택하거나, 새로운 대본을 등록하세요.</p>

    <div id="work-form" class="add-form">
      <input type="text" id="new-work-title" placeholder="작품 제목 입력">
      <input type="text" id="new-work-genre" placeholder="장르 또는 메모 입력">
      <button class="btn btn-primary" onclick="addWork()">작품 등록하기</button>
    </div>

    <div id="work-list" class="grid-list"></div>
  </section>

  <!-- STEP 2: 배역 선택 -->
  <section id="step-2" class="step-section">
    <div class="section-header">
      <h2>2. 배역 선택</h2>
      <button class="btn-add-toggle" onclick="toggleForm('role-form')">+ 새 배역 추가</button>
    </div>
    <p id="selected-work-title" class="desc"></p>

    <div id="role-form" class="add-form">
      <input type="text" id="new-role-name" placeholder="배역 이름 입력">
      <input type="number" id="new-role-cutline" placeholder="감독 설정 커트라인 % (기본 90)" min="50" max="100" value="90">
      <button class="btn btn-primary" onclick="addRole()">배역 등록하기</button>
    </div>

    <div id="role-list" class="grid-list"></div>

    <div class="btn-group">
      <button class="btn btn-secondary" onclick="goToStep(1)">작품 목록으로</button>
    </div>
  </section>

  <!-- STEP 3: 대사 및 BGM 선택 -->
  <section id="step-3" class="step-section">
    <div class="section-header">
      <h2>3. 대사 및 감정이입 노래 선택</h2>
      <button class="btn-add-toggle" onclick="toggleForm('line-form')">+ 새 대사 추가</button>
    </div>
    <p id="selected-role-title" class="desc"></p>

    <div id="line-form" class="add-form">
      <input type="text" id="new-line-situation" placeholder="상황 / 지문 입력">
      <textarea id="new-line-text" placeholder="연습할 대사 내용을 입력하세요."></textarea>
      <button class="btn btn-primary" onclick="addLine()">대사 저장하기</button>
    </div>
    
    <!-- 감정이입 음악 선택 (선택사항) -->
    <div class="music-box">
      <div class="music-header">🎵 감정이입 노래 선택 (선택 사항 - 촬영 전 재생)</div>
      <select id="bgm-select">
        <option value="" data-title="선택 안 함">노래 없이 바로 촬영하기</option>
        <option value="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" data-title="잔잔하고 아련한 피아노 선율">잔잔하고 아련한 피아노 선율 (멜로/감성)</option>
        <option value="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3" data-title="긴장감 넘치는 현악기">긴장감 넘치는 현악기 (갈등/비장함)</option>
        <option value="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3" data-title="설레고 경쾌한 어쿠스틱">설레고 경쾌한 어쿠스틱 (로맨스/일상)</option>
      </select>
    </div>

    <div id="line-list" class="grid-list"></div>

    <div class="btn-group">
      <button class="btn btn-secondary" onclick="goToStep(2)">배역 다시 고르기</button>
    </div>
  </section>

  <!-- STEP 4: BGM 감정이입 & 카메라 영상 촬영 화면 -->
  <section id="step-4" class="step-section">
    <h2>🎥 셀프 테이프 촬영 부스</h2>
    <p id="practice-info" class="desc"></p>

    <!-- 선택한 노래가 있을 경우 촬영 전 재생 컨트롤 -->
    <div id="practice-bgm-box" class="bgm-control-bar" style="display: none;">
      <div class="bgm-status-text">
        <span id="selected-bgm-name">🎵 선택된 노래: 없음</span>
        <span style="font-size: 0.75rem; color: #aaa;">촬영 전 노래를 들으며 감정을 잡아보세요</span>
      </div>
      <audio id="practice-bgm-player" controls></audio>
    </div>

    <!-- 대본 표시 영역 -->
    <div class="practice-stage">
      <span id="practice-situation" class="situation-tag">상황 설명</span>
      <p id="practice-line" class="script-text"></p>
    </div>

    <!-- 카메라 촬영 패널 -->
    <div class="camera-panel">
      <div class="video-wrapper">
        <video id="live-camera-preview" autoplay muted playsinline></video>
        <video id="recorded-video-player" controls playsinline style="display: none;"></video>
        <div class="rec-badge-overlay">
          <span id="rec-dot" class="dot"></span>
          <span id="rec-status">카메라 대기 중</span>
        </div>
      </div>

      <div class="btn-group">
        <button id="btn-start-rec" class="btn btn-primary" onclick="startVideoRecording()">🎥 촬영 시작</button>
        <button id="btn-stop-rec" class="btn btn-secondary" onclick="stopVideoRecording()" disabled>⏹ 촬영 종료</button>
      </div>

      <!-- 음성 인식된 대사 확인 -->
      <div id="recognized-text-box" class="recognized-box" style="display: none;">
        <strong>인식된 내 대사:</strong> <span id="recognized-result"></span>
      </div>

      <button id="btn-send-director" class="btn btn-success" style="width: 100%; display: none;" onclick="sendToDirector()">
        📤 감독에게 촬영 영상 전송하기
      </button>
    </div>

    <div class="btn-group">
      <button class="btn btn-secondary" onclick="exitCameraAndBack()">대사 다시 선택</button>
    </div>
  </section>

  <!-- STEP 5: 감독 전송 & 커트라인 판정(if 조건문) & 재촬영 버튼 생성(for 반복문) -->
  <section id="step-5" class="step-section">
    <h2>🎬 감독 심사 및 피드백</h2>
    <p id="director-role-cutline-info" class="desc"></p>

    <div class="director-box">
      <div style="font-size: 0.9rem; color: #aaa;">전송된 배우 셀프 테이프 영상:</div>
      <div class="video-wrapper">
        <video id="director-video-player" controls playsinline></video>
      </div>

      <!-- 연기 완성도(%) 결과 -->
      <div class="score-display">
        <div id="cutline-label" style="font-size: 0.85rem; color: #999; margin-bottom: 4px;">연기 완성도</div>
        <div id="accuracy-score" class="score-number">0%</div>
        <div id="accuracy-detail" style="font-size: 0.8rem; color: #888; margin-top: 6px;"></div>
      </div>

      <!-- 감독 코멘트 입력 영역 -->
      <div style="display: flex; flex-direction: column; gap: 8px;">
        <label style="font-size: 0.9rem; font-weight: 600; color: #ffd700;">✍️ 감독 코멘트 작성</label>
        <textarea id="director-comment-input" placeholder="커트라인 이상이면 격려 코멘트를, 이하라면 부족한 점(표정, 호흡, 발음 등)을 적어주세요."></textarea>
        <button class="btn btn-secondary" onclick="handleDirectorSubmit()">코멘트 등록 및 연기 완성도 판정</button>
      </div>

      <!-- 최종 판정 배너 (코멘트 등록 후 표시) -->
      <div id="final-verdict-area" style="display: none; flex-direction: column; gap: 12px; margin-top: 8px;">
        <div id="verdict-banner" class="result-banner"></div>
        <div style="background: #252525; padding: 14px; border-radius: 8px; border-left: 4px solid #ffd700;">
          <div id="comment-header-label" style="font-size: 0.8rem; color: #ffd700; margin-bottom: 4px;">감독 코멘트</div>
          <div id="saved-director-comment" style="font-size: 0.95rem; line-height: 1.5;"></div>
        </div>
        
        <!-- 통과 버튼 또는 for 반복문으로 생성된 재촬영 버튼들이 들어가는 영역 -->
        <div id="verdict-actions" class="btn-group"></div>
      </div>
    </div>
  </section>
</div>

<script>
  // 작품별 주요 인물, 감독 설정 커트라인(cutline), 대사 데이터
  const defaultScriptData = {
    "이 사랑 통역 되나요?": {
      genre: "로맨틱 코미디",
      roles: {
        "차무희 (글로벌 톱스타)": {
          cutline: 90,
          lines: [
            { situation: "해외 인터뷰 도중 돌발 행동을 하고 해맑게 웃으며", text: "어머, 통역사님! 방금 제 눈빛까지 같이 통역해 주셔야죠. 그게 오늘 인터뷰의 핵심인데!" },
            { situation: "자신의 진심을 못 알아주는 호진에게 답답함을 토로하며", text: "다른 나라 말은 그렇게 찰떡같이 알아듣는 사람이, 왜 내 말은 하나도 못 알아들어요? 일부러 그러는 거죠?" },
            { situation: "늦은 밤, 화려한 무대 뒤에서 지친 기색을 보이며", text: "사람들이 좋아하는 건 무대 위의 차무희지, 아무것도 없는 그냥 내가 아니에요. 통역사님도 마찬가지잖아요." },
            { situation: "호진에게 진심을 고백하기로 결심하고 단호하게", text: "이번엔 통역 필요 없어요. 내가 직접 말할 거니까, 딴청 피우지 말고 똑바로 들어요." }
          ]
        },
        "도라미 (무희의 또 다른 자아)": {
          cutline: 90,
          lines: [
            { situation: "거울 속 무희를 비웃듯 차갑고 직설적으로", text: "착각하지 마, 차무희. 저 남자가 친절한 건 네가 특별해서가 아니라 그냥 직업정신이 투철해서야." },
            { situation: "상처받기 두려워 도망치려는 무희를 다그치며", text: "또 도망치려고? 네가 언제까지 완벽한 척 가면을 쓰고 버틸 수 있을 것 같아?" },
            { situation: "호진을 향해 날카로운 경계심을 드러내며", text: "우리 무희 마음 흔들어 놓을 거면 지금 당장 그만둬요. 당신이 감당할 수 있는 사람이 아니니까." }
          ]
        },
        "주호진 (다중언어 통역사)": {
          cutline: 90,
          lines: [
            { situation: "무희의 엉뚱한 발언을 듣고 한숨을 쉬며 차분하게", text: "방금 그 말, 단어 그대로 토씨 하나 안 틀리고 통역해 드릴까요? 아니면 제가 적당히 수습해서 전달할까요?" },
            { situation: "선을 긋기 위해 일부러 냉정하고 사무적인 태도로", text: "나는 언어만 통역하는 사람입니다. 그쪽의 감정이나 행간의 의미까지 해석해 줄 의무는 없어요." },
            { situation: "자신의 감정을 자각한 후, 조용하지만 진심을 담아", text: "수많은 언어를 배웠지만, 당신이라는 사람의 언어는 여전히 너무 어렵습니다. 그래도 계속 번역해 보고 싶어졌어요." }
          ]
        },
        "히로 (일본 톱배우 / 무희의 파트너)": {
          cutline: 90,
          lines: [
            { situation: "무희에게 첫눈에 호감을 느끼고 능청스럽게 웃으며", text: "통역사님, 방금 제 심장이 뛰는 소리도 한국어로 번역이 됩니까? 무희 씨한테 꼭 전해줘야 하는데." },
            { situation: "호진의 미묘한 질투심을 눈치채고 여유롭게 도발하며", text: "통역사는 원래 두 사람 사이에 끼어드는 직업이 아니지 않나요? 지금은 우리 둘만의 대화인 것 같은데." },
            { situation: "자신의 마음을 솔직하게 고백하며 다정하게", text: "한국어는 아직 서툴지만 이 말만큼은 정확하게 연습했습니다. 나는 차무희 씨가 좋습니다." }
          ]
        }
      }
    },
    "미스터 션샤인": {
      genre: "시대극 / 멜로",
      roles: {
        "고애신 (조선 사대부 영애 / 의병)": {
          cutline: 90,
          lines: [
            { situation: "총을 겨누며 흔들림 없는 단호한 눈빛으로", text: "나는 불꽃으로 살다 죽을 것이오. 그러니 걱정 마시오, 동지. 그대는 그대의 길을 가시오." },
            { situation: "유진에게 한글을 배우며 순수하고 조심스럽게", text: "그대의 나라 말로 '러브'가 무엇이오? 총을 쏘는 것보다 어렵
