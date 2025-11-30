.. _`Troubleshooting`:

Troubleshooting
===============
This section describes some common issues that can arise and possible solutions.

Issue #1: Virtual Environment Not Activating
--------
**Description**: The virtual environment fails to activate or commands are not recognized.

**Solution**: 
- Ensure you're in the correct directory containing the virtual environment
- Use the full path: `source /path/to/venv/bin/activate`
- On Windows, use `venv\Scripts\activate`

Issue #2: Sphinx Build Fails
--------
**Description**: The `make html` command fails with import or configuration errors.

**Solution**:
- Verify Sphinx is installed in your virtual environment: `pip list | grep sphinx`
- Check that all .rst files have proper syntax and no missing dependencies
- Ensure you're running the command from the correct docs directory

Issue #3: GitHub Pages Not Updating
--------
**Description**: The documentation website doesn't show the latest changes.

**Solution**:
- Verify the gh-pages branch has the latest built documentation
- Check GitHub Pages settings in repository settings
- Ensure all files were properly committed and pushed to the gh-pages branch
- Wait a few minutes for GitHub to rebuild the site