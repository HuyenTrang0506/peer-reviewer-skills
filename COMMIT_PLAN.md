# Commit kiến trúc handbook và common library

Thay đổi hiện tại chưa được agent stage, commit hoặc push. Kiểm tra `git status`
trên checkout của bạn trước khi chạy các lệnh dưới đây; không dựa vào snapshot
commit cũ. Phần này thay thế hướng dẫn chia commit của giai đoạn tạo package ban đầu.

## Commit message đề xuất

```text
refactor(skills): centralize common review rules and add language skill

Organize both handbooks into parts, chapters, forms, and appendices.
Centralize reusable content in common and export standalone skill resources.
Add granular figure, readability, integrity, and professional language rules.
Clarify revision recommendations and preserve venue-specific workflows.
Add a small professional-office-language skill and verify shared exports.
```

Nên giữ lần chuyển cấu trúc này trong một commit: di chuyển chương, cập nhật link
và đổi allowlist đồng bộ phụ thuộc nhau. Commit từng nhóm file tùy ý có thể để lại
package thiếu tài liệu hoặc link hỏng.

## Kiểm tra và commit khi bạn sẵn sàng

```bash
python3 scripts/sync_shared_resources.py --check
python3 -m unittest discover -s tests -v
git diff --check
git status --short
git add common/ professional-office-language/ journal-peer-reviewer/ conference-peer-reviewer/ scripts/sync_shared_resources.py tests/test_shared_resources.py README.md METHODOLOGY.md COMMIT_PLAN.md
git diff --cached --stat
git commit -m "refactor(skills): centralize common review rules and add language skill" -m "Centralize reusable handbook resources, add granular FIG/READ/LANG/INT rules and a standalone professional-office-language skill, and clarify venue-specific revision recommendations."
```

Chỉ stage các đường dẫn đã xem diff và đúng phạm vi thay đổi. Không đưa manuscript,
cache hay nội dung review mật vào commit. Kiểm tra package không chứng minh chất
lượng review khoa học; bộ đánh giá hành vi vẫn chưa chạy. Không cần push trong
bước kiểm tra/commit này.

## Message riêng cho phần review articles

Nếu đã commit nền handbook/common ở trên, phần bổ sung tiếp theo có thể dùng:

```text
feat(review): add article-type rules for review manuscripts

Distinguish narrative, systematic, scoping, and meta-analytic synthesis.
Assess source accuracy, balanced coverage, consensus, and contribution.
Route both reviewer skills to shared REV rules and record slide provenance.
```

Nếu nền common vẫn chưa commit, giữ các file di chuyển, link và allowlist đồng bộ
trong cùng commit kiến trúc; không tạo commit module với nền phụ thuộc còn thiếu.

Message cho phần tinh chỉnh review formats và reviewer conduct:

```text
docs(review): calibrate coverage, recommendations, and reviewer commitments
```

Bao gồm REV theo perspective/trends/systematic, editorial stance, format limits,
summary tùy chọn, co-review permission và tách re-review need khỏi availability.
Chỉ tách thành commit riêng khi các thay đổi nền phụ thuộc đã được commit.
