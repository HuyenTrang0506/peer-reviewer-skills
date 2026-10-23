# Peer reviewer skills

Hai skill hỗ trợ người review có trách nhiệm kiểm chứng kết quả:

| Skill | Dùng khi |
| --- | --- |
| [journal-peer-reviewer](journal-peer-reviewer/SKILL.md) | Review cho journal: báo cáo tác giả/editor, recommendation theo journal và kiểm tra bản sửa. |
| [conference-peer-reviewer](conference-peer-reviewer/SKILL.md) | Review conference theo edition/track: rubric, confidence, rebuttal và discussion. |

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

## Tài liệu và kiểm tra

- [Phương pháp và kiến trúc](METHODOLOGY.md)
- [Nguồn và giới hạn kiểm chứng](journal-peer-reviewer/references/sources.md)
- [NISO/STM: thuật ngữ và phạm vi](journal-peer-reviewer/references/peer-review-standards.md)
- [Commit dần và xử lý GH007](COMMIT_PLAN.md)

Tài nguyên chung được chỉnh trong journal package rồi đồng bộ sang conference bằng allowlist; workflow, template, ví dụ và entry point riêng không bị ghi đè:

```bash
python3 scripts/sync_shared_resources.py --write
python3 scripts/sync_shared_resources.py --check
python3 -m unittest discover -s tests -v
```

Các script bảo trì chỉ dùng Python standard library. Kiểm tra package/công cụ đã được thực hiện; bộ đánh giá khoa học và các scenario hành vi chưa chạy. Ví dụ, ca kiểm tra và answer key là dữ liệu phát triển do tác giả soạn, không phải bằng chứng skill ngang chuyên gia hay cải thiện khả năng xuất bản. Nguồn bên ngoài có điều kiện sử dụng riêng; các liên kết tham khảo không cấp quyền tái phân phối chúng.
