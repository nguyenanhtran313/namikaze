import codecs

slides_html = """
      <!-- Slide 2: Phần 1 -->
      <section>
        <span class="subtitle">Phần 1: Kiến trúc tổng quan (Core Architecture)</span>
        <h2>1. Agent Tự Hành Là Gì?</h2>
        <p class="serif-quote">Các hệ thống AI này hoạt động qua giao diện <strong>CLI (Command Line Interface)</strong>. Thay vì dùng giao diện kéo-thả truyền thống (GUI), bạn dùng lệnh văn bản để yêu cầu AI tương tác trực tiếp với máy tính của mình.</p>
        <p>Bản chất của chúng là <strong>Autonomous Agents (Agent tự hành)</strong>. Chỉ với một yêu cầu (prompt), chúng sẽ tự động vạch kế hoạch, đọc file thư mục, tìm lỗi và tự viết code mà không cần bạn phải theo sát từng bước. Điểm khác biệt lớn nhất giữa chúng nằm ở <strong>khả năng lưu trữ trạng thái (Statefulness)</strong> và <strong>Trí nhớ dài hạn (Memory Persistence)</strong>.</p>
      </section>

      <!-- Slide 3: 3 Công Cụ -->
      <section>
        <span class="subtitle">Phần 1: Kiến trúc tổng quan (Core Architecture)</span>
        <h2>2. Bản chất cốt lõi của từng công cụ</h2>
        <div class="grid-3" style="gap: 15px;">
          <div class="card card-claude">
            <h3 class="highlight-green">Claude Code</h3>
            <p class="text-sm"><strong>Engine suy luận độc lập:</strong> Cực kỳ thông minh khi giải quyết các thuật toán nhiều bước. Tuy nhiên, AI này <strong>không lưu trạng thái (Stateless)</strong>, tức là nó sẽ quên quy chuẩn của dự án trừ khi bạn đưa cho nó một quyển "sổ tay" quy tắc (file tĩnh <code>CLAUDE.md</code>).</p>
          </div>
          <div class="card card-gemini">
            <h3 class="highlight-blue">Gemini CLI</h3>
            <p class="text-sm"><strong>Tương tác tức tốc (JIT Executor):</strong> Tối ưu cho tốc độ phản hồi cực nhanh. Tuy nhiên hệ thống <strong>thiếu đi bộ nhớ dài hạn</strong>, nó hiểu câu lệnh ngữ cảnh hiện tại rất tốt nhưng sẽ làm mới hoàn toàn trí nhớ khi bạn đóng cửa sổ Terminal.</p>
          </div>
          <div class="card card-anti">
            <h3 class="highlight-purple">AntiGravity</h3>
            <p class="text-sm"><strong>Hệ sinh thái kết hợp (Hybrid):</strong> Vừa có giao diện đẹp, vừa có sức mạnh truy cập hệ thống. Sức mạnh tuyệt đối nằm ở <strong>Bộ nhớ tự học (Knowledge Items - KIs)</strong>, khả năng vẽ biểu đồ trực quan (Artifacts) và tự lướt Web ẩn (Browser Subagent) để lấy dữ liệu.</p>
          </div>
        </div>
      </section>

      <!-- Slide 4: So sánh 1 -->
      <section>
        <span class="subtitle">Phần 2: So sánh tiêu chí Kỹ thuật (Technical Metrics)</span>
        <h2>3. Kiến trúc Hạ tầng & Cấu hình</h2>
        <table>
          <tr>
            <th>Tiêu chí Đánh giá</th>
            <th>Claude Code <span class="highlight-green">🟢</span></th>
            <th>Gemini CLI <span class="highlight-blue">🔵</span></th>
            <th>AntiGravity <span class="highlight-purple">🟣</span></th>
          </tr>
          <tr>
            <td><strong>Lõi Mô hình (Vendor)</strong></td>
            <td>Anthropic</td>
            <td>Google</td>
            <td class="highlight-purple">Google DeepMind</td>
          </tr>
          <tr>
            <td><strong>Giao thức Giao diện (Interface)</strong></td>
            <td>Chỉ gõ lệnh (Terminal CLI)</td>
            <td>Chỉ gõ lệnh (Terminal CLI)</td>
            <td class="highlight-purple">Kết hợp (Hybrid): Khung chat UI + Terminal ngầm</td>
          </tr>
          <tr>
            <td><strong>Định hướng Ngữ cảnh cục bộ</strong></td>
            <td>Theo tệp <code>CLAUDE.md</code></td>
            <td>Theo tệp <code>GEMINI.md</code></td>
            <td class="highlight-purple">Ghép nối tệp <code>_GEMINI.md</code> cùng Kho KIs tự học</td>
          </tr>
          <tr>
            <td><strong>Tệp Khởi tạo (Config Storage)</strong></td>
            <td><code>~/.claude.json</code> tại từng thư mục</td>
            <td><code>~/.gemini/</code></td>
            <td class="highlight-purple">Lưu trữ tập trung: <code>&lt;AppData&gt;/.gemini/antigravity/</code></td>
          </tr>
        </table>
      </section>

      <!-- Slide 5: So sánh 2 -->
      <section>
        <span class="subtitle">Phần 2: So sánh tiêu chí Kỹ thuật (Technical Metrics)</span>
        <h2>4. Bộ nhớ (Memory) & Lịch sử</h2>
        <table>
          <tr>
            <th>Tiêu chí Đánh giá</th>
            <th>Claude Code <span class="highlight-green">🟢</span></th>
            <th>Gemini CLI <span class="highlight-blue">🔵</span></th>
            <th>AntiGravity <span class="highlight-purple">🟣</span></th>
          </tr>
          <tr>
            <td><strong>Trí nhớ dài hạn (Long-term Context)</strong></td>
            <td>🔶 Thủ công. Team phải tự nhập tay các lỗi đã gặp vào file tĩnh.</td>
            <td>❌ Không có chế độ ghi nhớ ngoài từng phiên.</td>
            <td class="highlight-purple">✅ Tự động trích lọc kinh nghiệm lỗi vào Kho tri thức (KIs).</td>
          </tr>
          <tr>
            <td><strong>Lịch sử Phiên làm việc (Session)</strong></td>
            <td>✅ Khởi tạo bộ đệm xem lại (Short-term cache logs).</td>
            <td>❌ Mất hoàn toàn lịch sử hội thoại khi đóng Terminal.</td>
            <td class="highlight-purple">✅ Sao lưu toàn bộ Log thao tác siêu chi tiết vào <code>overview.txt</code></td>
          </tr>
          <tr>
            <td><strong>Mã định danh (Session UUID)</strong></td>
            <td>✅ Có ID rõ ràng để tiếp tục luồng hội thoại cũ.</td>
            <td>❌ Các phiên độc lập hoàn toàn.</td>
            <td class="highlight-purple">✅ Quản lý từng dự án qua các ID mã hóa tĩnh (UUID) tách biệt.</td>
          </tr>
          <tr>
            <td><strong>Cấp bậc Đọc hiểu (Hierarchical Scope)</strong></td>
            <td>Chỉ đọc theo cây thư mục (Subfolder Tree).</td>
            <td>Giới hạn trong thư mục làm việc (Namespace cục bộ).</td>
            <td class="highlight-purple">Ưu tiên cấp bậc KIs → Log cũ → File Code hiện hành.</td>
          </tr>
        </table>
      </section>

      <!-- Slide 6: So sánh 3 -->
      <section>
        <span class="subtitle">Phần 2: So sánh tiêu chí Kỹ thuật (Technical Metrics)</span>
        <h2>5. Quy trình chạy (Execution) & Đầu ra</h2>
        <table style="font-size: 0.8em;">
          <tr>
            <th>Tiêu chí Đánh giá</th>
            <th>Claude Code <span class="highlight-green">🟢</span></th>
            <th>Gemini CLI <span class="highlight-blue">🔵</span></th>
            <th>AntiGravity <span class="highlight-purple">🟣</span></th>
          </tr>
          <tr>
            <td><strong>Phân tác vụ (Orchestration)</strong></td>
            <td>Tự động phân rã I/O lệnh trực tiếp trên máy.</td>
            <td>Gọi API thẳng để biên dịch file độc lập.</td>
            <td class="highlight-purple">Chạy đa nhiệm (Async), tự động replace nhiều dòng độc lập cực thông minh.</td>
          </tr>
          <tr>
            <td><strong>Chuẩn tích hợp ngoài (MCP Protocol)</strong></td>
            <td>✅ Tương thích mạnh mẽ (Là tác giả của chuẩn này).</td>
            <td>🔶 Đang xây dựng dưới dạng thử nghiệm (Experimental).</td>
            <td class="highlight-purple">✅ Tích hợp hoàn hảo thông qua <code>mcp_config.json</code>.</td>
          </tr>
          <tr>
            <td><strong>Báo cáo Giao diện (Artifacts UI)</strong></td>
            <td>❌ Text Terminal khô khan (Một chiều).</td>
            <td>❌ Text Terminal thuần túy (Một chiều).</td>
            <td class="highlight-purple">✅ Kết xuất slide băng chuyền, biểu đồ Markdown và Bảng so sánh code màu đỏ/xanh (Git Diff).</td>
          </tr>
          <tr>
            <td><strong>Đọc hiểu Web (Browser Subagent)</strong></td>
            <td>❌ Phải copy code HTML bằng tay mới hiểu nội dung Web.</td>
            <td>❌ Không đọc được link Web ngoại lai.</td>
            <td class="highlight-purple">✅ Tự bật Chrome vô hình, nhấp chuột và quay video (file <code>.webp</code>) quá trình thao tác.</td>
          </tr>
        </table>
      </section>

      <!-- Slide 7: Vai trò -->
      <section>
        <span class="subtitle">Phần 3: Phân rã Khái niệm (Concept Breakdown)</span>
        <h2>6. Phân định: Agent Tự Hành vs Trợ Lý Gõ Code (IDE Assist)</h2>
        <p style="margin-bottom: 25px;">⚠️ Đừng nhầm lẫn giữa một <strong>Tác tử tự hành (Autonomous Agent)</strong> chuyên nghiệp và một <strong>Trợ lý gợi ý code trên phần mềm (IDE Code Assist)</strong>. Chúng thuộc hai phân lớp phục vụ hoàn toàn khác nhau.</p>
        <table style="font-size: 0.7em;">
          <tr>
            <th>Tiêu chí Phân định</th>
            <th>AI Tự Hành (Autonomous Agent) [VD: Claude Code]</th>
            <th>AI Trợ Lý Code (IDE Assist) [VD: Gemini Code Assist]</th>
          </tr>
          <tr>
            <td><strong>Quy trình xử lý (Pipeline Model)</strong></td>
            <td><strong>Hoàn tất trọn gói (End-to-End Orchestration):</strong> Nhận 1 đề bài, tự mò dự án, tự chạy Terminal và Fix bug cho tới khi Output hoàn chỉnh.</td>
            <td><strong>Bơm mã cục bộ (Context Injection):</strong> Hiểu đoạn mã bạn đang tự viết tay, rồi đề xuất hàm tự động điền nốt (Autocomplete) cho câu đó.</td>
          </tr>
          <tr>
            <td><strong>Tính tương tác</strong></td>
            <td>Giao nhiệm vụ xong, bạn có thể đi pha cafe và chờ tiến trình (Bất đồng bộ).</td>
            <td>Như một trợ lý đúng nghĩa, bám theo thao tác gõ phím trực tiếp của bạn (Trực tiếp thời gian thực).</td>
          </tr>
          <tr>
            <td><strong>Sức mạnh cốt lõi</strong></td>
            <td class="highlight-green"><strong>Suy luận logic (Reasoning):</strong> Vạch thuật toán chính xác từ số 0, tránh các lỗi sai vớ vẩn hệ thống.</td>
            <td class="highlight-blue"><strong>Chứa bộ nhớ lớn (Massive Context Window):</strong> Đọc một lần cả nghìn tệp Code, phù hợp nhất để review Code, bắt lỗi gõ sai biến.</td>
          </tr>
        </table>
      </section>

      <!-- Slide 8: AntiGravity 1 -->
      <section>
        <span class="subtitle">Phần 4: Vũ khí của Nền tảng (Platform Features)</span>
        <h2>7. Kiến trúc sức mạnh AntiGravity (Phần 1)</h2>
        <div class="grid-2">
          <div>
            <h3><span class="badge bg-purple">1</span> Cơ Chế Vòng Lặp Tự Hành (Autonomous Loop)</h3>
            <ul class="text-sm">
              <li><strong>Phân tích hệ thống (Planning Engine):</strong> Chia một bài toán Phân tích Data Data phức tạp thành các mốc nhỏ thay vì đâm đầu vào code ngay.</li>
              <li><strong>Móc nối thao tác (Kernel Handshake):</strong> Tạo vòng lặp ngầm: Viết mã SQL ⟶ chạy qua terminal nội bộ ⟶ nếu Terminal chê lỗi, lấy thông báo về tự chữa lỗi ⟶ Giao file chuẩn cuối cùng cho bạn.</li>
            </ul>
          </div>
          <div>
            <h3><span class="badge bg-purple">2</span> Bộ Não Tri Thức Ẩn (Knowledge Items - KIs)</h3>
            <ul class="text-sm">
              <li>Mỗi lần team DA chật vật sửa một lỗi SQL phức tạp, hệ thống tự lấy đó làm pattern để tạo ra file kỹ năng <strong>KIs</strong> không thể tẩy xóa.</li>
              <li>Lần sau gặp task tương tự, hệ thống tự truy nạp kho trí tuệ KIs này, không bao giờ lập lại lỗi 2 lần hay phải để con người nhắc luật (Zero-shot bypass).</li>
            </ul>
          </div>
        </div>
      </section>

      <!-- Slide 9: AntiGravity 2 -->
      <section>
        <span class="subtitle">Phần 4: Vũ khí của Nền tảng (Platform Features)</span>
        <h2>8. Kiến trúc sức mạnh AntiGravity (Phần 2)</h2>
        <div class="grid-2">
          <div>
            <h3><span class="badge bg-purple">3</span> Tác Tử Trình Duyệt Ngầm (Browser Subagent)</h3>
            <ul class="text-sm">
              <li>Chạy một Trình duyệt ở chế độ Vô Hình (Headless DOM). AI tự thao tác cuộn chuột, Click nút, giải mã HTML của trang web công ty thay vì bó tay.</li>
              <li>Đặc biệt có khả năng quay nén phim màn hình (đuôi <code>.webp</code>) cho toàn bộ thao tác, nhằm đảm bảo minh bạch (Audit Trails) cho dự án.</li>
            </ul>
          </div>
          <div>
            <h3><span class="badge bg-purple">4</span> Kết xuất Giao Diện Đồ Họa (Artifact Engine)</h3>
            <ul class="text-sm">
              <li>Không ném hàng nghìn chữ thẳng vào mắt User. Biến Schema bảng Database phức tạp thành Sơ Đồ Thiết Kế chuẩn (Mermaid Vector Diagrams) cực dễ nhìn.</li>
              <li>Kích hoạt tính năng Diff Block: Bóc tách mảng nào bị xóa (Đỏ) và thêm mới (Xanh Lá) rành mạch, rất tiện cho các sếp Audit (Kiểm toán Code) thay vì soi mỏi mắt.</li>
            </ul>
          </div>
        </div>
      </section>

      <!-- Slide 10: Tips DA -->
      <section>
        <span class="subtitle">Phần 5: Bí quyết áp dụng công việc (Practical Tips)</span>
        <h2>9. Các Tips Tinh chỉnh Ngữ Cảnh Dành Cho DA Team</h2>
        <div style="background: #fafafa; padding: 25px; border-radius: 8px; border: 1px solid #ddd;">
          <ul style="margin:0; padding-left: 20px; font-size: 0.85em; line-height: 1.7;">
            <li>💡 <strong>Chèn Keyword Đồ Họa Cấp Cao:</strong> AI mặc định thiết kế khá đơn điệu. Hãy ép AI tạo UI xịn bằng bộ lệnh: <em>"Apply UI: Premium contrast palette, European Typography Inter font, Dynamic state transitions"</em> đồ họa của slide slide hay report sẽ lập tức trông rất chuyên nghiệp.</li>
            <li>💡 <strong>Cập Nhật Trí Khôn KIs Thủ Công:</strong> Nếu ra được mảng biểu đồ rất tối ưu, hãy ra lệnh luôn: "Lưu pattern biểu đồ chuẩn này vào KIs Library cho dự án sau."</li>
            <li>💡 <strong>Neo Ngữ Cảnh Xuyên Suốt Không Phai (Workspace root):</strong> Cẩm nang của Data Team cần được nhét vào file tĩnh <code>_GEMINI.md</code> đặt ở gốc folder dự án. AI sẽ không bao giờ sai quy tắc Naming Convention của Leader đề ra.</li>
            <li>⚠️ <strong>Tuyệt đối không mang API ngoài vào tự đổi (BYOK Warning):</strong> Tính năng phân tán của DeepMind Agentic chỉ tối ưu cực đại khi chạy qua Engine tích hợp sẵn. Mang Token API cá nhân vào ép chạy sẽ phá vỡ toàn bộ cấu trúc kết nối Tool của Agent.</li>
          </ul>
        </div>
      </section>

      <!-- Slide 11: Ecosystem 1 -->
      <section>
        <span class="subtitle">Phần 6: Giao thức Máy Mở (Open Protocols)</span>
        <h2>10. Kiến trúc Phổ quát MCP (Model Context Protocol)</h2>
        <p class="serif-quote highlight-blue" style="border-left-color: #1565c0; font-size: 1.15em;">"MCP hoạt động như ổ cắm chuyển đổi đa năng, giúp bộ xử lý trần trụi của Trại AI (LLMs) chạm trực tiếp vào Kho Lưu Trữ Dữ Liệu của doanh nghiệp."</p>
        <p><strong>Bản chất Technical:</strong> Khác với hồi AI bị nhốt trong lồng Sandbox chỉ biết đọc Chat, chuẩn Mở MCP (thông qua JSON-RPC Context API) đã cho AI một đôi bàn tay để nối đến Cổng Server máy khách. Kết quả: AI có thể chủ động đào dữ liệu từ Kho BigQuery, gửi biến cảnh báo vượt quá KPI lên thẳng Slack nội bộ hay chèn File Report vào nền tảng Notion của Team.</p>
      </section>

      <!-- Slide 12: Ecosystem 2 -->
      <section>
        <span class="subtitle">Phần 6: Khớp Nối Tool Doanh Nghiệp (Tooling Ecosystem)</span>
        <h2>11. Phân Tầng Hệ Cấu Trúc Khớp Nối (MCP Nodes)</h2>
        <table style="font-size: 0.65em;">
          <tr>
            <th>Application Server (Nền Tảng Đích)</th>
            <th>Cung Cấp Chức năng (Exposed API Endpoints)</th>
            <th>Trường Hợp Ứng Dụng Đời Thực (Usecases)</th>
          </tr>
          <tr>
            <td><strong>Google BigQuery Server</strong></td>
            <td><code>query_data(), retrieve_schema()</code><br><span style="color:#777">Xử lý vòng lặp SQL Vector Arrays</span></td>
            <td>Tự động Mapping các cấu trúc bảng lạ, nhúng lệnh SQL tìm doanh thu MKT theo khung giờ trực tiếp từ Kho BigQuery về hệ máy nội bộ làm Data Analytics.</td>
          </tr>
          <tr>
            <td><strong>Slack Notification API</strong></td>
            <td><code>post_channel_webhook(), stream_media()</code><br><span style="color:#777">Thông báo sự kiện Asynchronous TCP Hooks</span></td>
            <td>Khi System báo KPI chệch quỹ đạo quá cảnh báo ngầm, AI kết nối cổng Slack gửi báo động cực mạnh tag riêng tên Leader dự án.</td>
          </tr>
          <tr>
            <td><strong>Brave Search / Local Filesystem</strong></td>
            <td><code>web_scrape_engine() / read_write_dir()</code><br><span style="color:#777">Đọc Ghi File Không Trực Tiếp</span></td>
            <td>Bỏ qua công đoạn con người phải thao tác Copy-Paste. AI tự đọc CSV Local rà soát File Logs Data tĩnh và tiến hành thay đổi Content theo batch độc lập.</td>
          </tr>
        </table>
      </section>

      <!-- Slide 13: Workflow MCP -->
      <section>
        <span class="subtitle">Phần 6: Sức Mạnh Tự Hóa Toàn Trình (End-to-End Orchestrations)</span>
        <h2>12. Mô phỏng Kiến Trúc Hệ Sinh Thái MCP</h2>
        <div class="card" style="border: 2px solid #6a1b9a;">
          <p class="text-sm">🗣️ Trigger từ người dùng: <em>"Truy xuất kho Google BigQuery chỉ số Volume Q3, viết mã Python xuất Graph Analysis ra ảnh và dán tự động vào kho lưu trữ Notion."</em></p>
          <ul class="text-sm" style="list-style: none; padding-left: 0; margin-top:20px;">
            <li style="margin-bottom: 12px;">✅ <strong>Bước 1 - Khởi chạy:</strong> Tác Tử liên kết API Server của MCP BigQuery, vượt bảo mật, rút Matrix Data thô cần thiết.</li>
            <li style="margin-bottom: 12px;">✅ <strong>Bước 2 - Trình Dịch Chuyển (Conversion):</strong> Mở thư viện Native Python Mathplotlib ngầm, dựng ma trận hình ảnh Biểu đồ sắc nét để kết xuất tệp đồ họa.</li>
            <li>✅ <strong>Bước 3 - Cập Bến:</strong> Xác thực kết nối qua mạng với Notion API System Server, Up File thành Report khép kín chuẩn chỉ. <strong>(Tự Động Hóa 0% hao hụt người).</strong></li>
          </ul>
        </div>
      </section>

      <!-- PHẦN 7: THỰC CHIẾN MỞ RỘNG (CLAUDE CODE) -->

      <!-- Slide 14: Header Phần 7 -->
      <section data-background="#6a1b9a">
        <h1 style="color: white; border: none; font-size: 3em;">PART 7</h1>
        <h2 style="color: white; border-color: white;">Nâng Cao: Giải Mã Kho Vũ Khí Claude Code</h2>
        <p style="color: rgba(255,255,255,0.7);">Quản trị câu lệnh điều tiết Hệ thống (Meta-Commands), thiết lập ranh giới làm việc (Workspace Policy) và Kích hoạt tự động hóa vòng đời (Hooks).</p>
      </section>

      <!-- Slide 15: Bài 1 - /compact (Tính năng nâng cao) -->
      <section>
        <span class="subtitle">Phần 7 — Module 1: Quản trị Ranh Giới Ngữ Cảnh (Context Bound Management)</span>
        <h2>13. Thực thi Lệnh Thuận Tiện: <code>/compact</code></h2>
        <p>Bản chất kỹ thuật là <strong>Thu Gọn Số Lượng Token (Token Compaction)</strong>, làm sạch bộ nhớ để mô hình không tốn công đọc các thông báo rác không quan trọng.</p>
        <div class="grid-2" style="gap: 15px;">
          <div class="card" style="padding: 20px;">
            <p class="text-sm" style="margin-bottom: 5px;"><strong>1. Focus Compaction (Nén tái định hướng trọng số)</strong></p>
            <div class="terminal-box" style="margin-top: 0; padding: 10px;">
              <span class="terminal-cmd">/compact prioritize bảng JOIN User</span>
            </div>
            <p class="text-sm" style="margin-top: 8px;">Dẹp đi những đoạn chat báo lỗi vụn vặt rác lề phía trên để bộ óc Mô hình tập trung vào Trọng Số (Weights) chính.</p>
          </div>
          <div class="card" style="padding: 20px;">
            <p class="text-sm" style="margin-bottom: 5px;"><strong>2. Milestone Compaction (Nén chốt chặn hoàn thành)</strong></p>
            <div class="terminal-box" style="margin-top: 0; padding: 10px;">
              <span class="terminal-cmd">/compact Milestone checkpoint: Xong Auth, Chuyển sang Phase Query System.</span>
            </div>
            <p class="text-sm" style="margin-top: 8px;">Xả bộ nhớ Context Logs cũ sau khi hoàn thành. Lưu lại mỗi cốt lõi trước đưa Project rẽ nhánh Branch mới.</p>
          </div>
        </div>
        <p class="text-sm" style="margin-top: 15px;"><strong>💡 Điều Kiện Kích Hoạt lúc rủi ro:</strong> Ngay khi AI mắc triệu chứng Ảo Giác Thuật Toán (Hallucination) do Tràn giới hạn Tokens Memory Limits.</p>
      </section>

      <!-- Slide 15b: Phân biệt các lệnh -->
      <section>
        <span class="subtitle">Phần 7 — Module 1: Quản trị Phân luồng Câu lệnh Trực Tiếp</span>
        <h2>14. Phân Luồng Meta-Commands</h2>
        <table>
          <tr>
            <th>Meta-Command Terminal</th>
            <th>Cơ Chế Kích Hoạt (Pipeline Trigger)</th>
            <th>Trường Hợp Ứng Dụng Hữu Dụng (Usecase Implementation)</th>
          </tr>
          <tr>
            <td><strong><span class="highlight-green">/compact</span></strong></td>
            <td>Tóm tắt & Nén Token (Context Shrinking)</td>
            <td>Duy trì cấu trúc cốt lõi tiến độ hệ thống Database (Project Memory) trong khi giảm tải CPU/GPU Delay, không thoát Session Thread khởi điểm.</td>
          </tr>
          <tr>
            <td><strong><span class="highlight-purple">/rewind</span></strong></td>
            <td>Cuộn lại thao tác State Rollback</td>
            <td>Mô phỏng Undo Memory Version State. Khôi phục tình trạng bộ đệm Mô Hình trước khi Commit Logic sai hỏng làm lag Context, an toàn và dễ làm.</td>
          </tr>
          <tr>
            <td><strong><span class="highlight-blue">/clear</span></strong></td>
            <td>Hủy Phiên Làm Việc (Session Purge)</td>
            <td>Reset Zero-shot hoàn chỉnh. Phù hợp tẩy trắng Vector Token Local Environment System khi khởi động hệ Test Framework toàn bộ.</td>
          </tr>
        </table>
      </section>

      <!-- Slide 16: Bài 2 - .claude Folder -->
      <section>
        <span class="subtitle">Phần 7 — Module 2: Lớp Cấu Hình Cục Bộ (Local Policy System)</span>
        <h2>15. Định vị Workspace Policy qua Folder <code>.claude</code></h2>
        <p>Kho chứa Quy Tố (Rule sets) áp đặt ranh giới chuẩn mực riêng ở thư mục làm việc, ép LLM tuân thủ.</p>
        <div class="terminal-box" style="font-size: 0.55em;">
          <span style="color: #6a9955;">// Framework Logic Config: .claude/rules.md</span><br>
          - Bắt buộc phải Output kiểu <span style="color: #ce9178;">snake_case</span> parameters.<br>
          - Xuất File Validation Data Data Schema chuẩn mực vào File <span style="color: #ce9178;">.csv</span> container objects format.<br>
          <br>
          <span style="color: #6a9955;">// Truyền Inject Mảng State Mapping: .claude/memory.json</span><br>
          { "last_exception_catch": "Backend Network BigQuery Protocol Timeout", "resolution_injection": "Append LIMIT 100 clauses to Root Nodes" }
        </div>
        <p class="text-sm" style="margin-top: 15px;">Khởi động cơ chế "Ép hiểu luật mới cho gõ phím". AI sẽ đọc System Metadata Policy trước tiên khi bạn ra lệnh, chặn việc đi lệch hướng ngay từ đầu.</p>
      </section>

      <!-- Slide 17: Bài 3 - Slash Commands -->
      <section>
        <span class="subtitle">Phần 7 — Module 3: Tác Vụ Nội Tĩnh Độc Lập</span>
        <h2>16. Giao thức Lệnh Slash (Slash Commands Endpoints)</h2>
        <p>Bypass Prompt System dài dòng bằng đường tắt (In-memory triggers) tối ưu Token Stream API.</p>
        <div class="grid-2">
          <div class="card" style="border-top-color: #000;">
            <h3><code>/cost</code></h3>
            <p class="text-sm">Hiển thị Giám sát Bill (Monitoring Metric API).</p>
            <div class="terminal-box" style="margin-top:5px; padding:10px;">
              <span class="terminal-output">Billing Core Output: $0.45 Authored Response Tokens Evaluated (Current Session)</span>
            </div>
          </div>
          <div class="card" style="border-top-color: #f00;">
            <h3><code>/bug</code></h3>
            <p class="text-sm">Kiểm Toán Tĩnh (Static Compiler Linter/Pre-check).</p>
            <div class="terminal-box" style="margin-top:5px; padding:10px;">
              <span class="terminal-output">AST Linter Hook: Phân giải Validation Failure tại folder_main/query.sql<br>Initiating Context Auto-Fixing Automation...</span>
            </div>
          </div>
        </div>
      </section>

      <!-- Slide 18: Bài 4 - Hooks -->
      <section>
        <span class="subtitle">Phần 7 — Module 4: Tự Động Hóa Tiến Trình Điểm Cắt (Lifecycle Hooks Automation)</span>
        <h2>17. Listeners Hooks (Hàm Lắng Nghe Sự Kiện)</h2>
        <p>Chèn cấu trúc chạy nền (Event Listeners Payload) và Điểm cắt Thực thi (Execution Breakpoints) vào vòng đời Code generation.</p>
        <div class="terminal-box" style="font-size: 0.6em;">
          <span style="color: #6a9955;">// Lifecycle Config Manifest File: .claude/hooks.json</span><br>
          {<br>
          &nbsp;&nbsp;"post-save": "sql-formatter --write",<br>
          &nbsp;&nbsp;"pre-run": "python check_privacy_anomalies_layer.py"<br>
          }
        </div>
        <div class="card" style="margin-top:20px;">
          <p class="text-sm"><strong>Ứng Dụng Hữu Ích Cực Độ:</strong> Ở Hook "post-save" End-of-Stream, tự dưng mã Agent sinh SQL xong. Bạn chả cần làm gì, nền tảng bắn Process Pipeline (Terminal Script) kích chạy công cụ căn chỉnh Formats (<code>sql-formatter</code>). Trả ra Codebase vuông vức, sạch chuẩn mà chả tốn 10 giây Manual Human Interaction.</p>
        </div>
      </section>

      <!-- Slide 19: Cảm ơn -->
      <section>
        <h1 style="text-align: center; font-size: 3.5em; letter-spacing: 0.1em; margin-bottom: 10px;">THANK YOU</h1>
        <p style="text-align: center; color: #777; font-size: 0.8em; font-weight: 600; text-transform: uppercase;">
          OMD Data Analytics Team <br> Core Technology Framework - 2026
        </p>
      </section>
"""

with codecs.open('d:/_AntiGravity/_playground/AI_Coding_Tools_Slides.html', 'r', 'utf-8') as f:
    content = f.read()

start_marker = "<!-- Slide 2: Phần 1 -->"
end_marker = "</div>\n  </div>\n\n  <script>"

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx != -1 and end_idx != -1:
    new_content = content[:start_idx] + slides_html.strip() + "\n    " + content[end_idx:]
    with codecs.open('d:/_AntiGravity/_playground/AI_Coding_Tools_Slides.html', 'w', 'utf-8') as f:
        f.write(new_content)
    print("Replaced successfully!")
else:
    print(f"Could not find markers: {start_idx}, {end_idx}")

