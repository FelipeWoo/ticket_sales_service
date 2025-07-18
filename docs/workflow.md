# Project Workflow — ticket\_sales\_service

A complete breakdown of development tasks, testing activities, and recommended commit messages per stage.

---

## MVP — Minimal Viable Product

Goal: Create a working ticket with SQLite and generate a public-facing PDF.

### Setup and Scaffolding

| Activity                                     | Commit                                         |
| -------------------------------------------- | ---------------------------------------------- |
| Initialize project folder and base structure | chore: initialize project structure            |
| Add .gitignore and basic config files        | chore: add base config files                   |
| Create initial SQLite schema for tickets     | feat: create initial SQLite schema for tickets |

### Core Logic

| Activity                                         | Commit                                             |
| ------------------------------------------------ | -------------------------------------------------- |
| Implement function to calculate total and tax    | feat: implement total and tax calculation function |
| Implement create\_ticket with UUID and timestamp | feat: add basic ticket creation logic              |
| Insert ticket record into SQLite                 | feat: insert ticket record into SQLite             |

### PDF Output

| Activity                                             | Commit                                        |
| ---------------------------------------------------- | --------------------------------------------- |
| Generate PDF from ticket public data                 | feat: generate PDF from ticket public fields  |
| Create function to extract public fields from ticket | feat: extract public fields for printable PDF |

### Basic Testing

| Activity                                     | Commit                                        |
| -------------------------------------------- | --------------------------------------------- |
| Add test for total and tax calculation       | test: verify tax and total calculation logic  |
| Add test for ticket creation and UUID format | test: confirm ticket creation and UUID format |

---

## Stage 1 — Input and Validation

### Validation

| Activity                                     | Commit                                                |
| -------------------------------------------- | ----------------------------------------------------- |
| Add validation for required ticket fields    | feat: add input validation for required ticket fields |
| Validate structure and content of items list | feat: enforce structure on items in ticket payload    |
| Add tax and pricing sanity checks            | feat: reject invalid tax and pricing inputs           |

### Tests

| Activity                                 | Commit                                             |
| ---------------------------------------- | -------------------------------------------------- |
| Add test to reject malformed ticket data | test: reject malformed or incomplete ticket inputs |
| Validate allowed payment method types    | test: enforce valid payment method enumeration     |

---

## Stage 2 — Ticket Management

### Storage and Retrieval

| Activity                                            | Commit                                          |
| --------------------------------------------------- | ----------------------------------------------- |
| Implement get\_ticket\_by\_id function              | feat: retrieve ticket record by ticket\_id      |
| Implement ticket cancellation with reason           | feat: add cancellation logic with reason        |
| Add support for public and private field separation | feat: separate public and private ticket fields |

### Utilities

| Activity                                   | Commit                                           |
| ------------------------------------------ | ------------------------------------------------ |
| Add UUID and timestamp generator functions | chore: add utility functions for ticket metadata |
| Define Ticket class with to\_dict method   | feat: define Ticket class with to\_dict method   |

### Tests

| Activity                                   | Commit                                         |
| ------------------------------------------ | ---------------------------------------------- |
| Test ticket retrieval from database        | test: retrieve and validate full ticket object |
| Test ticket cancellation and status update | test: update ticket status to cancelled        |

---

## Stage 3 — SQL Query Interface

### SQL Interface

| Activity                               | Commit                                      |
| -------------------------------------- | ------------------------------------------- |
| Create view for public ticket fields   | feat: create SQLite view for public tickets |
| Add safe SQL query executor            | feat: implement safe SQL query executor     |
| Add filters for date, status, location | feat: support ticket filtering by SQL       |

### Tests

| Activity                               | Commit                                                 |
| -------------------------------------- | ------------------------------------------------------ |
| Test filtering by date range using SQL | test: SQL query by date range returns expected results |
| Reject unsafe SQL commands             | test: reject unsafe SQL statements in query interface  |

---

## Stage 4 — PDF Templates

### Formatting

| Activity                             | Commit                                     |
| ------------------------------------ | ------------------------------------------ |
| Improve PDF layout and formatting    | feat: improve visual layout of PDF tickets |
| Add store name or logo to PDF output | feat: include branding in PDF templates    |
| Add QR code with ticket ID to PDF    | feat: embed QR code with ticket ID in PDF  |

### Tests

| Activity                               | Commit                                        |
| -------------------------------------- | --------------------------------------------- |
| Ensure PDF contains only public fields | test: ensure no private data leaks into PDF   |
| Verify generated PDF file is valid     | test: verify PDF file is created and readable |

---

## Stage 5 — Export and Reports

### Data Export

| Activity                                | Commit                                             |
| --------------------------------------- | -------------------------------------------------- |
| Export tickets to CSV by date range     | feat: export ticket data as CSV file               |
| Add report grouping by day and location | feat: generate report summary by date and location |

### Tests

| Activity                                    | Commit                                   |
| ------------------------------------------- | ---------------------------------------- |
| Validate exported CSV structure and headers | test: verify exported CSV structure      |
| Validate accuracy of grouped totals         | test: verify grouped report logic by day |

---

## Stage 6 — Audit and Integrity

### Security and Integrity

| Activity                                         | Commit                                                |
| ------------------------------------------------ | ----------------------------------------------------- |
| Generate SHA256 hash for each ticket             | feat: generate SHA256 audit hash for each ticket      |
| Validate ticket integrity on retrieval           | feat: validate ticket integrity using hash comparison |
| Optional: implement hash chaining for audit logs | feat: support hash chaining for audit logs            |

### Tests

| Activity                                       | Commit                                                    |
| ---------------------------------------------- | --------------------------------------------------------- |
| Recalculate hash and compare with stored value | test: validate stored audit hash matches recomputed value |
| Detect data modification via failed hash check | test: detect data corruption via audit hash mismatch      |

---

## Stage 7 — CLI Interface

### CLI Interface

| Activity                              | Commit                                                |
| ------------------------------------- | ----------------------------------------------------- |
| Add CLI command to create ticket      | feat: create CLI tool for ticket creation             |
| Add list, cancel, and export commands | feat: extend CLI with listing and export capabilities |
| Add documentation for CLI usage       | docs: add CLI usage instructions                      |

### Tests

| Activity                      | Commit                                   |
| ----------------------------- | ---------------------------------------- |
| Test ticket lifecycle via CLI | test: end-to-end ticket workflow via CLI |

---

## Optional: Makefile or Automation

| Activity                                       | Commit                                            |
| ---------------------------------------------- | ------------------------------------------------- |
| Add Makefile for test and run commands         | chore: add Makefile with test and run targets     |
| Add make command for PDF and ticket generation | chore: add Makefile entry to generate demo ticket |

---

