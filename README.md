# Peer reviewer skills

Hai skill review và một skill ngôn ngữ dùng độc lập:

| Skill | Dùng khi |
| --- | --- |
| [journal-peer-reviewer](journal-peer-reviewer/SKILL.md) | Review cho journal: báo cáo tác giả/editor, recommendation theo journal và kiểm tra bản sửa. |
| [conference-peer-reviewer](conference-peer-reviewer/SKILL.md) | Review conference theo edition/track: rubric, confidence, rebuttal và discussion. |
| [professional-office-language](professional-office-language/SKILL.md) | Soạn/sửa email, memo, report và review comments cho rõ ràng, lịch sự; giữ nguyên dữ kiện và mức độ chắc chắn. |

## Dùng skill

Mỗi thư mục là một package tự chứa tài liệu/template cần thiết. Với Codex, sao chép thư mục skill muốn dùng vào `$CODEX_HOME/skills/` hoặc `~/.codex/skills/` nếu chưa đặt biến đó; giữ các file con. Nếu đã có thư mục cùng tên, xem khác biệt trước khi thay thế. Skill cài mới sẽ dùng được từ lượt tiếp theo. Không cần cài thư mục `scripts/` hay `tests/` để đọc/dùng skill.

Ví dụ yêu cầu:

```text
Use $journal-peer-reviewer to review the authorized manuscript against
the named journal's reviewer instructions and prepare a working draft.

Use $conference-peer-reviewer to review the authorized submission for
the named conference edition and track, using the supplied rubric.
```

Trước khi xử lý manuscript chưa công bố, cần xác nhận quyền, policy AI/confidentiality, xung đột lợi ích và phạm vi. Skill không tự gửi report, liên hệ tác giả/editor hay sửa manuscript. Khi thiếu kiến thức phương pháp, quy trình enrichment chủ động tìm/tải tài liệu skill công khai để tham khảo; không tự chạy mã tải về hoặc đưa nội dung mật vào tìm kiếm.

## Đọc như một quyển sách

Mỗi skill có mục lục riêng: [Journal handbook](journal-peer-reviewer/references/CONTENTS.md) và [Conference handbook](conference-peer-reviewer/references/CONTENTS.md). Cấu trúc thư mục theo bốn phần, 10 chương, bộ biểu mẫu và phụ lục:

```text
SKILL.md                           Điểm vào và các điều kiện thiết yếu
references/
  CONTENTS.md                      Mục lục, mục đích và cách đọc từng chương
  01-foundations/                  Phần I: rulebook, tiêu chuẩn, assignment
  02-appraisal/                    Phần II: đọc, thẩm định, chuyên ngành
  03-reporting/                    Phần III: kiểm chứng nhận xét, viết report
  04-review-rounds/                Phần IV: ví dụ review và vòng phản hồi
  appendices/                     Nguồn, protocol đánh giá, answer key
assets/                           Biểu mẫu và dữ liệu phát triển
```

Chương 5 bổ sung thẩm định theo loại bài và từng section, với module REV riêng cho narrative/systematic/scoping review và meta-analysis; Chương 9 hướng dẫn overview, strengths, major/minor comments và recommendation. Thứ tự chương giúp hiểu quy trình; khi review chỉ mở chương cần dùng. Answer key và dữ liệu đánh giá không dùng làm evidence cho manuscript.

## Cấu trúc rule

Hai entry point dùng cùng [rulebook](journal-peer-reviewer/references/01-foundations/rulebook.md), có bản sao trong mỗi package để cài độc lập:

| Lớp | Cách áp dụng | Ví dụ |
| --- | --- | --- |
| **H — Hard rule** | Bắt buộc khi điều kiện áp dụng; thiếu điều kiện thì giới hạn/dừng bước liên quan. | Không bịa evidence; không nhận đã review toàn bài khi mới đọc trích đoạn; không ép trích dẫn cá nhân. |
| **V — Venue-conditional** | Bắt buộc khi policy đúng venue/edition/track/stage được xác định là áp dụng. | Rubric, supplement, audience, rebuttal, AI/disclosure. Chưa rõ thì ghi nhận giới hạn, không tự đặt luật. |
| **S — Soft default** | Điều chỉnh theo assignment, giữ H và V; chỉ giải thích thay đổi có ảnh hưởng đáng kể. | Thứ tự đọc, số lượt đọc, bố cục report/workbook, ngân sách tìm skill ban đầu. |

Mỗi rule có mã, điều kiện áp dụng và cách xử lý khi chưa đáp ứng. Workflow dẫn từ binding venue → authorization/scope → appraisal → adjudication/update → output → human handoff; thứ tự thao tác có thể linh hoạt. Đây là phân loại thiết kế của repository, không phải phân loại do NISO/STM ban hành.

## Tài liệu và kiểm tra

- [Phương pháp và kiến trúc](METHODOLOGY.md)
- [Thư viện chung và các rule module](common/README.md)
- [Nguồn và giới hạn kiểm chứng](journal-peer-reviewer/references/appendices/sources.md)
- [NISO/STM: thuật ngữ và phạm vi](journal-peer-reviewer/references/01-foundations/peer-review-standards.md)
- [Commit message và lệnh kiểm tra](COMMIT_PLAN.md)

Tài nguyên chung được chỉnh trong `common/` rồi xuất sang cả hai reviewer package
bằng allowlist. LANG rules còn được xuất sang skill office-language. Bản sao trong
package phục vụ cài độc lập; không chỉnh trực tiếp. Workflow venue, report template,
ví dụ, mục lục và entry point riêng không bị ghi đè:

```bash
python3 scripts/sync_shared_resources.py --write
python3 scripts/sync_shared_resources.py --check
python3 -m unittest discover -s tests -v
```

Các script bảo trì chỉ dùng Python standard library. Kiểm tra package/công cụ đã được thực hiện; bộ đánh giá khoa học và các scenario hành vi chưa chạy. Ví dụ, ca kiểm tra và answer key là dữ liệu phát triển do tác giả soạn, không phải bằng chứng skill ngang chuyên gia hay cải thiện khả năng xuất bản. Nguồn bên ngoài có điều kiện sử dụng riêng; các liên kết tham khảo không cấp quyền tái phân phối chúng.
