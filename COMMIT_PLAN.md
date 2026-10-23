# Commit dần trên máy của bạn

Agent chưa tạo commit, stage hay push thay bạn. Ngày 2026-10-23, lịch sử local có commit journal `ca772fc` do bạn tạo; conference và công cụ/tài liệu vẫn chưa commit tại thời điểm kiểm tra. Chạy ở thư mục gốc, xem `git status` và `git diff --cached --stat` trước mỗi commit. Không chạy lại một nhóm đã hoàn tất chỉ để tái tạo lịch sử.

## Xử lý GH007 trước lần push tiếp theo

GitHub đang chặn email riêng tư trong commit, không phải lỗi nén/đẩy object hay mật khẩu. Đã đặt đúng `user.name` và Gmail bạn yêu cầu trong `.git/config` của repo này; global config không bị đổi. Thay config không sửa author/committer của commit cũ. Không ghi lại email cá nhân trong tài liệu này vì cấu hình đã nằm local.

Để tiếp tục dùng Gmail đã chọn, mở [GitHub Settings → Emails](https://github.com/settings/emails) và bỏ **Block command line pushes that expose my email** nếu bạn chấp nhận công khai email trong lịch sử commit, rồi chạy lại `git push`. Cần thay đổi trên tài khoản GitHub; chỉnh local config không thể thay cho bước này. Không cần force-push để thử lại một push đã bị từ chối.

Nếu muốn giữ kín email thay vì dùng Gmail, lấy đúng địa chỉ GitHub `noreply` tại trang đó. Việc đổi author/committer của các commit local đã có sẽ thay hash và cần được bạn chủ động yêu cầu hoặc tự thực hiện sau khi kiểm tra lịch sử. Agent không tự amend/rewrite commit và không tắt bảo vệ tài khoản. Không chỉ đổi email của commit cuối rồi mặc định lịch sử trước đó đã được làm sạch.

Tài liệu GitHub kiểm tra ngày 2026-10-23: [cấu hình email cho một repository](https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address), [chặn push làm lộ email](https://docs.github.com/en/account-and-profile/how-tos/email-preferences/blocking-command-line-pushes-that-expose-your-personal-email-address).

## Bổ sung journal sau commit đầu tiên

Các thay đổi mới làm rõ desk screening, similarity score và xung đột lợi ích phát sinh. Để giữ commit đầu tiên nguyên vẹn, tạo một commit bổ sung khi bạn sẵn sàng:

```bash
git add journal-peer-reviewer/
git diff --cached --stat
git commit -m "docs(journal): clarify editorial screening and integrity concerns"
```

## 1. Journal skill và nền phương pháp — nhóm ban đầu đã commit

Bao gồm quy trình journal, thẩm định chuyên ngành, ví dụ/re-review, NISO/STM, nguồn PMC, prompt tìm/tải kiến thức chuyên ngành và bộ tình huống phát triển. Skill này tự dùng được mà không cần conference package. Các lệnh sau là tham khảo cho checkout chưa có nhóm này; không chạy lại trên commit journal đã tạo. `.gitignore` vẫn có thể chưa được commit nếu bạn chỉ add thư mục journal.

```bash
git add .gitignore journal-peer-reviewer/
git diff --cached --stat
git commit -m "feat(journal): add evidence-based journal peer review skill"
```

## 2. Conference skill

Bao gồm luồng riêng theo edition/track, rubric và confidence, rebuttal/discussion, ví dụ và template riêng. Các tài nguyên dùng chung được đóng gói tại chỗ để cài skill độc lập.

```bash
git add conference-peer-reviewer/
git diff --cached --stat
git commit -m "feat(conference): add venue-specific review and rebuttal workflow"
```

## 3. Đồng bộ tài nguyên và tài liệu dự án

Bao gồm công cụ phát hiện/đồng bộ tài nguyên chung, kiểm tra hành vi đồng bộ và tài liệu kiến trúc/commit.

```bash
git add .gitignore README.md scripts/ tests/ METHODOLOGY.md COMMIT_PLAN.md
git diff --cached --stat
git commit -m "chore: document skill architecture and verify shared resources"
```

## Kiểm tra trước khi commit

```bash
python3 scripts/sync_shared_resources.py --check
python3 -m unittest discover -s tests -v
git diff --check
```

Các kiểm tra trên xác nhận tính nhất quán của package/công cụ; chúng không đo chất lượng nhận xét khoa học. Bộ đánh giá reviewer vẫn chưa chạy. Không đưa manuscript chưa công bố hoặc cache theo tác vụ vào các commit. Không cần push trong quá trình chia commit; push khi bạn chủ động chọn.
