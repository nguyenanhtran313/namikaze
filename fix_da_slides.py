import codecs
import re

file_path = 'd:/_AntiGravity/_playground/AI_Coding_Tools_Slides.html'
with codecs.open(file_path, 'r', 'utf-8') as f:
    content = f.read()

replacements = [
    # Slide 2
    ('Agent Tự Hành Là Gì?', 'Autonomous Agent Xử Lý Data Như Thế Nào?'),
    ('Bạn dùng lệnh văn bản để yêu cầu AI tương tác trực tiếp với máy tính của mình.', 
     'Bạn thiết lập cấu trúc ngôn ngữ tự nhiên để yêu cầu luồng AI trích xuất data.'),
    ('Bản chất của chúng là <strong>Autonomous Agents (Agent tự hành)</strong>.', 
     'Bản chất của loại Tool này là <strong>AI Tự Động (Autonomous Agent)</strong>.'),
    ('Điểm khác biệt lớn nhất giữa chúng nằm ở <strong>khả năng lưu trữ trạng thái (Statefulness)</strong> và <strong>Trí nhớ dài hạn (Memory Persistence)</strong>.</p>',
     'Điểm khác biệt lớn nhất giữa chúng nằm ở <strong>khả năng nhớ trạng thái Database</strong> và <strong>Lưu Trí nhớ dài hạn (Memory Persistence)</strong>.</p>\n        <div style="font-size: 0.5em; text-align: left; color: #888; border-top: 1px solid #ddd; padding-top: 10px; margin-top: 30px;">\n          *Chú thích từ DA: Không cần quan tâm tới "CLI" hay "Lưu trạng thái Node". Hệ thống Agent sẽ âm thầm lo các việc xử lý kĩ thuật phía sau (background processing), Data Analyst chỉ việc cung cấp ngôn ngữ tự nhiên và theo dõi quá trình chạy Data.\n        </div>'),

    # Slide 4
    ('Định hướng Ngữ cảnh cục bộ', 'Phạm vi Context Cục bộ'),
    ('Kho KIs tự học', 'Cơ sở Kiến thức (KIs)'),

    # Slide 5
    ('Cấp bậc Đọc hiểu (Hierarchical Scope)', 'Phân Mức Độ Dò Ngữ Cảnh (Context Hierarchy)'),
    ('Giới hạn trong thư mục làm việc (Namespace cục bộ)', 'Giới hạn trong những file nhỏ đang được xử lý.'),

    # Slide 6
    ('Kết xuất slide băng chuyền', 'Render Carousel ảnh cuộn'),
    ('Trình duyệt ở chế độ Vô Hình (Headless DOM)', 'Trình duyệt Web Scraping chạy nền'),

    # Slide 7
    ('Phân rã Khái niệm (Concept Breakdown)', 'Làm rõ Định Nghĩa (Concept Breakdown)'),
    ('Agent Tự Hành vs Trợ Lý Gõ Code', 'AI Tự Động Toàn Trình vs Tool Auto-Gợi Ý Code'),
    ('Tác tử tự hành (Autonomous Agent)', 'Hệ thống tự động (Autonomous Agent)'),
    ('Hoàn tất trọn gói (End-to-End Orchestration)', 'Vận hành toàn trình (E2E)'),
    ('Bơm mã cục bộ (Context Injection)', 'Mớm thông tin cục bộ (Context Injection)'),

    # Slide 8
    ('Cơ Chế Vòng Lặp Tự Hành (Autonomous Loop)', 'Chu Kỳ Vận Hành Tự Động (Autonomous Loop)'),
    ('Móc nối thao tác (Kernel Handshake)', 'Tích hợp Hệ Thống Xử Lý'),
    ('Bộ Não Tri Thức Ẩn (Knowledge Items - KIs)', 'Cơ Sở Kiến Thức (Knowledge Items - KIs)'),

    # Slide 9
    ('Tác Tử Trình Duyệt Ngầm', 'Trình Duyệt Đi Thu Thập Ngầm'),
    ('Chế độ Vô Hình (Headless DOM)', 'Chế độ Nền (Hidden Background)'),
    ('Kết xuất Giao Diện Đồ Họa', 'Sinh Các Bảng Tương Tác'),
    ('rất tiện cho các sếp Audit (Kiểm toán Code)', 'thuận lợi bắt bệnh mà không cần mò mẫn'),
    ('<!-- Slide 10: Tips DA -->', '<div style="font-size: 0.5em; text-align: left; color: #888; border-top: 1px solid #ddd; padding-top: 10px; margin-top: 20px;">\n          *Chú thích từ DA: Diff Block (Màu đỏ/Màu xanh lá) là cách màn hình soi cho ta thấy: Trước đây AI viết lệnh JOIN bảng bị sai (khoanh đỏ), ngay dòng dưới là lệnh JOIN mới được thay (màu xanh lá). Rất dễ Review bằng mắt thường mà không phải là dân Code cứng.\n        </div>\n      </section>\n\n      <!-- Slide 10: Tips DA -->'),

    # Slide 10
    ('Neo Ngữ Cảnh Xuyên Suốt Không Phai', 'Lưu Trữ Context Vĩnh Viễn'),
    ('Naming Convention', 'Tiêu chuẩn Naming Parameters'),

    # Slide 11
    ('chạm trực tiếp vào Kho Lưu Trữ Dữ Liệu của doanh nghiệp', 'móc mượt mà với Kho Lưu Trữ Dữ Liệu (Warehouse) của cty'),

    # Slide 12
    ('Phân Tầng Hệ Cấu Trúc Khớp Nối (MCP Nodes)', 'Mô Phỏng Các Hệ Khớp Nối MCP'),
    ('Xử lý vòng lặp SQL Vector Arrays', 'Phân tích Data Schema Trực quan'),
    ('Thông báo sự kiện Asynchronous TCP Hooks', 'Bắn thông báo Asynchronous Slack'),
    ('Đọc Ghi File Không Trực Tiếp', 'Tự động Tracking Lịch Sử Excel'),
    ('<!-- Slide 13: Workflow MCP -->', '<div style="font-size: 0.5em; text-align: left; color: #888; border-top: 1px solid #ddd; padding-top: 10px; margin-top: 20px;">\n          *Chú thích từ DA: Các yếu tố như "TCP Hooks" hay "Vector Arrays" là cấu hình ngầm System, DA chúng ta không cần gõ hay thao tác chúng bao giờ. Hãy hiểu đơn giản là: MCP giúp AI "giơ tay" mượn tạm Data BigQuery và "giơ tay" gửi tin nhắn Slack cho Team thay DA làm.\n        </div>\n      </section>\n\n      <!-- Slide 13: Workflow MCP -->'),

    # Slide 13
    ('Sức Mạnh Tự Hóa Toàn Trình (End-to-End Orchestrations)', 'Quy Trình Tự Động Hóa Toàn Trình (End-to-End)'),
    ('Trình Dịch Chuyển (Conversion)', 'Khối Chuyển Đổi Model'),
    ('Mathplotlib', 'matplotlib'),
    ('tệp đồ họa.</p>', 'tệp đồ họa. <strong>*Lưu ý: System sẽ tạm ngưng chờ Data Analyst ấn xác thực thông qua UI, trước khi chạy cổng Post Báo cáo.</strong></p>'),

    # Slide 14
    ('Kho Vũ Khí', 'Mảng Lệnh'),
    ('Quản trị câu lệnh điều tiết Hệ thống (Meta-Commands)', 'Sử dụng lệnh tắt hỗ trợ ngữ cảnh'),

    # Slide 15
    ('Quản trị Ranh Giới Ngữ Cảnh (Context Bound Management)', 'Xoá Đệm Nhớ Hệ Thống'),

    # Slide 15b
    ('Quản trị Phân luồng Câu lệnh Trực Tiếp', 'Quản Trị Terminal Trực Tiếp'),
    ('Cuộn lại thao tác State Rollback', 'Trục xuất Lỗi (Rollback)'),
    ('Phù hợp tẩy trắng Vector Token Local Environment System khi khởi động hệ Test Framework toàn bộ.', 'Giúp xoá hoàn toàn cache cũ vướng bận, giải phóng không gian tư duy cho Data Agent, giống như dọn dẹp bộ nhớ đệm.'),

    # Slide 16
    ('Lớp Cấu Hình Cục Bộ (Local Policy System)', 'Lớp Thiết Lập Môi Trường Workspace'),
    ('Quy Tố', 'Luật/Rules'),
    ('Tác Vụ Nội Tĩnh Độc Lập', 'Tính năng Slash Commands'),

    # Slide 18
    ('Tự Động Hóa Tiến Trình Điểm Cắt (Lifecycle Hooks Automation)', 'Xử Lý Nền tự động hóa với Hooks'),
    ('Chèn cấu trúc chạy nền (Event Listeners Payload)', 'Gắn Script dọn dẹp Code'),
    ('<!-- Slide 19: Cảm ơn -->', '<div style="font-size: 0.5em; text-align: left; color: #888; border-top: 1px solid #ddd; padding-top: 10px; margin-top: 20px;">\n          *Chú thích cho Phần Lệnh (Slide 14 đến 18): Dân Data không phải gõ bất kỳ câu lệnh điều khiển khô khan nào. Tool AI bản mới nhất như AntiGravity có giao diện trực quan hỗ trợ sẵn hoặc tự động quyết định lúc nào cần dùng /rewind lúc lỗi.\n        </div>\n      </section>\n\n      <!-- Slide 19: Cảm ơn -->')
]

for old_str, new_str in replacements:
    content = content.replace(old_str, new_str)

with codecs.open(file_path, 'w', 'utf-8') as f:
    f.write(content)

print(f"Applied {len(replacements)} replacements successfully to HTML file.")
