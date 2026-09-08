# Git Safety Rules — Company Brain

1. **Pre-Flight Verification**:
   - Before applying changes or switching branches, always run:
     ```bash
     git status && git branch && git diff
     ```
   - Confirm your working tree is clean or that existing work is safely isolated.

2. **Prohibited Operations**:
   - **Never** perform `git reset --hard` or `git checkout .` without explicit human authorization.
   - **Never** perform `git push --force` to shared or main branches.
   - **Never** drop or overwrite stashes containing uncommitted work.
   - **Never** modify files in unrelated repositories or directories.

3. **Atomic, Descriptive Commits**:
   - Commit changes atomically by feature or bugfix.
   - Use clear conventional commit prefixes: `feat:`, `fix:`, `refactor:`, `test:`, `docs:`, `chore:`.
   - Post-change check:
     ```bash
     git diff && git status && <run relevant test suite>
     ```
