# Common reviewer library

Đây là **nguồn chỉnh sửa duy nhất** cho các chương, rule module, biểu mẫu và
dữ liệu phát triển dùng chung. Thư mục này không phải skill để cài riêng.

```text
references/
  01-foundations/   Rulebook, NISO/STM, integrity và overlap
  02-appraisal/     Phương pháp, từng section, FIG/READ rules, domain lenses
  03-reporting/     Adjudication, viết report, LANG rules
  appendices/       Nguồn, protocol đánh giá và answer key
assets/            Workbook, prompt enrichment, dữ liệu phát triển
```

Các module nhỏ:

- [FIG: figures/tables](references/02-appraisal/figures-and-tables.md)
- [READ: manuscript language/readability](references/02-appraisal/language-and-readability.md)
- [LANG: professional wording](references/03-reporting/professional-language.md)
- [INT: integrity/overlap](references/01-foundations/integrity-and-overlap.md)
- [REV: review articles](references/02-appraisal/review-articles.md)

Mỗi module ghi mã rule, H/V/S, điều kiện áp dụng và cách xử lý. Chúng triển khai
[rulebook](references/01-foundations/rulebook.md); rule ID không thay cho evidence.

Chỉnh file trong `common/`, rồi chạy từ gốc repository:

```bash
python3 scripts/sync_shared_resources.py --write
python3 scripts/sync_shared_resources.py --check
python3 -m unittest discover -s tests -v
```

Script dùng allowlist để xuất bản sao vào cả hai reviewer package. LANG còn được
xuất sang `professional-office-language/references/professional-language.md`.
Không chỉnh trực tiếp các bản sao: thay đổi sẽ bị báo drift và bị ghi đè khi
đồng bộ. Các bản sao cho phép cài từng skill độc lập, không phụ thuộc thư mục
anh em hoặc symlink. Đồng bộ không tự xóa file ngoài allowlist.

Entry point, metadata, mục lục, workflow venue, report template và worked example
vẫn thuộc từng skill, không được ghi đè bởi đồng bộ. Skill office-language có
entry point riêng và chỉ dùng LANG; nó không thẩm định phương pháp khoa học.

Đọc nguồn hoặc protocol đánh giá khi cần. Answer key và dữ liệu phát triển không
được đưa vào review thông thường hoặc inference context của đánh giá mù.
