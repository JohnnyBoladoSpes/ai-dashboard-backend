from django.db import models


class Business(models.Model):
    INDUSTRY_CHOICES = [
        ("retail", "Retail"),
        ("food", "Food & Beverages"),
        ("tech", "Technology"),
        ("fashion", "Fashion"),
        ("health", "Health & Wellness"),
        ("other", "Other"),
    ]

    name = models.CharField(max_length=255)
    industry = models.CharField(
        max_length=50, choices=INDUSTRY_CHOICES, default="other"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class PlatformAccount(models.Model):
    PLATFORM_CHOICES = [
        ("instagram", "Instagram"),
        ("facebook", "Facebook"),
        ("twitter", "Twitter"),
        ("tiktok", "TikTok"),
        ("other", "Other"),
    ]

    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    platform = models.CharField(max_length=50, choices=PLATFORM_CHOICES)
    username = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.business.name} - {self.platform}"


class Post(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    platform_account = models.ForeignKey(
        PlatformAccount, on_delete=models.CASCADE, null=True, blank=True
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post by {self.business.name} on {self.created_at.strftime('%Y-%m-%d')}"


class EngagementMetric(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    likes = models.PositiveIntegerField(default=0)
    comments = models.PositiveIntegerField(default=0)
    shares = models.PositiveIntegerField(default=0)
    collected_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Metrics for {self.post.business.name} - {self.collected_at.strftime('%Y-%m-%d')}"


class Insight(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    analysis_type = models.CharField(max_length=100)
    raw_data = models.JSONField()
    insights = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.business.name} - {self.analysis_type}"
