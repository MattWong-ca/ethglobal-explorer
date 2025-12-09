# 🚀 GitHub Actions Automation Setup

This guide will help you set up automated data updates using GitHub Actions that run on GitHub's servers completely automatically.

## ✨ What Gets Automated

- **Daily**: Project updates (3 AM UTC)
- **Weekly**: Hackathon discovery (Sundays, 1 AM UTC)  
- **Monthly**: Full data refresh (1st day, 2 AM UTC)
- **Daily**: System health checks (12 PM UTC)
- **Manual**: On-demand script execution

## 🔧 Setup Instructions

### 1. Configure Repository Secrets

Go to your GitHub repository → Settings → Secrets and variables → Actions

Add these **Repository Secrets**:

#### Required Secrets
```
SUPABASE_URL
Your Supabase project URL (e.g., https://xxxxx.supabase.co)

SUPABASE_SERVICE_KEY  
Your Supabase service role key (starts with eyJ...)
```

#### Optional Secrets (for notifications)
```
DISCORD_WEBHOOK_URL
Discord webhook URL for notifications (optional)

EMAIL_SMTP_SERVER
SMTP server for email notifications (e.g., smtp.gmail.com)

EMAIL_FROM
Email address to send notifications from

EMAIL_TO  
Email address to receive notifications

EMAIL_PASSWORD
Email password or app-specific password
```

### 2. Enable GitHub Actions

1. Go to your repository → Actions tab
2. If Actions are disabled, click "I understand my workflows, go ahead and enable them"
3. The workflows will be automatically detected from `.github/workflows/`

### 3. Test the Setup

#### Option A: Manual Test
1. Go to Actions tab → "🎛️ Manual Data Update"
2. Click "Run workflow"
3. Select scripts to run (e.g., `05_scrape_hackathons.py`)
4. Click "Run workflow"

#### Option B: Health Check
1. Go to Actions tab → "🩺 System Health Check"
2. Click "Run workflow"  
3. Select "full" check type
4. Click "Run workflow"

## 📅 Automation Schedules

| Workflow | Schedule | Purpose |
|----------|----------|---------|
| **Data Update** | Daily 3 AM UTC | Update project data |
| **Data Update** | Weekly Sun 1 AM UTC | Discover new hackathons |  
| **Data Update** | Monthly 1st 2 AM UTC | Full data refresh |
| **Health Check** | Daily 12 PM UTC | System monitoring |

## 🎛️ Manual Controls

### Quick Manual Updates
Go to Actions → "🎛️ Manual Data Update" → Run workflow

**Common Script Combinations:**
- **Projects Only**: `02_scrape_projects.py,03_upload_projects.py`
- **Hackathons Only**: `05_scrape_hackathons.py,04a_upload_hackathons.py`
- **Full Refresh**: `05_scrape_hackathons.py,01_upload_prizes.py,02_scrape_projects.py,03_upload_projects.py`
- **Prizes Only**: `01_upload_prizes.py`

### Available Scripts
- `01_upload_prizes.py` - Upload prize information
- `02_scrape_projects.py` - Scrape projects from showcase
- `03_upload_projects.py` - Upload scraped projects to database
- `04a_upload_hackathons.py` - Upload hackathon data  
- `05_scrape_hackathons.py` - Scrape hackathon information

## 📊 Monitoring & Notifications

### Discord Notifications
If `DISCORD_WEBHOOK_URL` is configured:
- ✅ Successful runs (monthly refresh only)
- ❌ Failed runs
- 🚨 Health check failures
- 📊 Statistics (records processed, duration)

### Email Notifications  
If email secrets are configured:
- Manual update completions
- Critical failures

### GitHub Actions Interface
- View all runs: Repository → Actions tab
- Download logs and artifacts
- Re-run failed workflows
- Cancel running workflows

## 🛠️ Troubleshooting

### Common Issues

**"Secret not found" errors**
- Verify secrets are set in repository settings
- Check secret names match exactly (case-sensitive)

**Database connection failures**
- Verify `SUPABASE_URL` and `SUPABASE_SERVICE_KEY`
- Test connection with health check workflow

**Scraping timeouts**
- Web scraping can be slower on GitHub runners
- Scripts have 2-hour timeout by default

**Chrome/ChromeDriver issues**
- GitHub runners have Chrome pre-installed
- Workflows automatically configure headless Chrome

### Debug Mode
Run manual updates with "Enable debug logging" checked for detailed output.

### View Logs
1. Go to Actions tab
2. Click on workflow run
3. Click on job name
4. Expand log sections to see details

## 🔒 Security Best Practices

- ✅ Use repository secrets for sensitive data
- ✅ Service keys have minimal required permissions
- ✅ Workflows run in isolated GitHub containers
- ✅ No sensitive data in logs
- ✅ Artifacts auto-expire after retention period

## 📈 Cost Considerations

GitHub Actions usage:
- **Public repos**: Unlimited minutes
- **Private repos**: 2,000 minutes/month free
- Estimated usage: ~30-60 minutes/month for this automation

## 🎯 Advanced Configuration

### Modify Schedules
Edit cron expressions in `.github/workflows/data-update.yml`:
```yaml
schedule:
  - cron: '0 3 * * *'  # Daily at 3 AM UTC
  - cron: '0 1 * * 0'  # Weekly on Sundays at 1 AM UTC  
  - cron: '0 2 1 * *'  # Monthly on 1st at 2 AM UTC
```

### Add Environment-Specific Configurations
Create separate secrets for different environments:
- `SUPABASE_URL_STAGING`
- `SUPABASE_URL_PRODUCTION`

### Custom Notifications
Modify Discord webhook payloads in workflow files to customize messages.

## ✅ Verification Checklist

After setup, verify:
- [ ] Repository secrets are configured
- [ ] Health check workflow passes
- [ ] Manual test workflow completes successfully  
- [ ] Discord/email notifications work (if configured)
- [ ] Data appears in your database
- [ ] Scheduled workflows show in Actions tab

## 🆘 Support

If you encounter issues:
1. Check the workflow logs in Actions tab
2. Run health check workflow to identify problems
3. Verify all secrets are configured correctly
4. Test manual workflows before relying on scheduled runs

---

**🎉 Once configured, your ETHGlobal Explorer will automatically stay up-to-date with fresh data from GitHub's servers!**