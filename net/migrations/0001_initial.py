# Generated by Django 3.0.7 on 2020-06-25 15:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publicly_visible', models.CharField(choices=[('y', 'yes'), ('n', 'no')], default='y', max_length=1)),
                ('title', models.CharField(max_length=64)),
                ('description', models.CharField(blank=True, max_length=1024)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Calibration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ramin', models.FloatField()),
                ('ramax', models.FloatField()),
                ('decmin', models.FloatField()),
                ('decmax', models.FloatField()),
                ('x', models.FloatField()),
                ('y', models.FloatField()),
                ('z', models.FloatField()),
                ('r', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='CommentReceiver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DiskFile',
            fields=[
                ('collection', models.CharField(default='misc', max_length=40)),
                ('file_hash', models.CharField(max_length=40, primary_key=True, serialize=False, unique=True)),
                ('size', models.PositiveIntegerField()),
                ('file_type', models.CharField(max_length=256, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EnhanceVersion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('topscale', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Flag',
            fields=[
                ('name', models.CharField(max_length=56, primary_key=True, serialize=False)),
                ('explanation', models.CharField(blank=True, max_length=2048)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='FlaggedUserImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flagged_time', models.DateTimeField(auto_now=True)),
                ('flag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='net.Flag')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('width', models.PositiveIntegerField(null=True)),
                ('height', models.PositiveIntegerField(null=True)),
                ('disk_file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='net.DiskFile')),
                ('display_image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='image_display_set', to='net.Image')),
                ('thumbnail', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='image_thumbnail_set', to='net.Image')),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('S', 'Success'), ('F', 'Failure')], max_length=1)),
                ('error_message', models.CharField(max_length=256)),
                ('queued_time', models.DateTimeField(null=True)),
                ('start_time', models.DateTimeField(null=True)),
                ('end_time', models.DateTimeField(null=True)),
                ('calibration', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='job', to='net.Calibration')),
            ],
        ),
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allow_commercial_use', models.CharField(choices=[('y', 'yes'), ('n', 'no'), ('d', 'use default')], default='d', max_length=1)),
                ('allow_modifications', models.CharField(choices=[('y', 'yes'), ('sa', 'yes, but share alike'), ('n', 'no'), ('d', 'use default')], default='d', max_length=2)),
                ('license_name', models.CharField(max_length=1024)),
                ('license_uri', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='ProcessSubmissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.IntegerField()),
                ('watchdog', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SkyLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nside', models.PositiveSmallIntegerField()),
                ('healpix', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SkyObject',
            fields=[
                ('name', models.CharField(max_length=1024, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publicly_visible', models.CharField(choices=[('y', 'yes'), ('n', 'no')], default='y', max_length=1)),
                ('url', models.URLField(blank=True, null=True)),
                ('parity', models.PositiveSmallIntegerField(choices=[(2, 'try both simultaneously'), (0, 'positive'), (1, 'negative')], default=2)),
                ('scale_units', models.CharField(choices=[('arcsecperpix', 'arcseconds per pixel'), ('arcminwidth', 'width of the field (in arcminutes)'), ('degwidth', 'width of the field (in degrees)'), ('focalmm', 'focal length of the lens (for 35mm film equivalent sensor)')], default='degwidth', max_length=20)),
                ('scale_type', models.CharField(choices=[('ul', 'bounds'), ('ev', 'estimate +/- error')], default='ul', max_length=2)),
                ('scale_lower', models.FloatField(blank=True, default=0.1, null=True)),
                ('scale_upper', models.FloatField(blank=True, default=180, null=True)),
                ('scale_est', models.FloatField(blank=True, null=True)),
                ('scale_err', models.FloatField(blank=True, null=True)),
                ('positional_error', models.FloatField(blank=True, null=True)),
                ('center_ra', models.FloatField(blank=True, null=True)),
                ('center_dec', models.FloatField(blank=True, null=True)),
                ('radius', models.FloatField(blank=True, null=True)),
                ('tweak_order', models.IntegerField(blank=True, default=2, null=True)),
                ('downsample_factor', models.PositiveIntegerField(blank=True, default=2, null=True)),
                ('use_sextractor', models.BooleanField(default=False)),
                ('crpix_center', models.BooleanField(default=False)),
                ('invert', models.BooleanField(default=False)),
                ('image_width', models.IntegerField(blank=True, default=0, null=True)),
                ('image_height', models.IntegerField(blank=True, default=0, null=True)),
                ('via_api', models.BooleanField(default=False)),
                ('original_filename', models.CharField(max_length=256)),
                ('submitted_on', models.DateTimeField(auto_now_add=True)),
                ('processing_started', models.DateTimeField(null=True)),
                ('processing_finished', models.DateTimeField(null=True)),
                ('processing_retries', models.PositiveIntegerField(default=0)),
                ('error_message', models.CharField(max_length=2048, null=True)),
                ('album', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='net.Album')),
                ('comment_receiver', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='net.CommentReceiver')),
                ('disk_file', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='submissions', to='net.DiskFile')),
                ('license', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='net.License')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='submissions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('text', models.CharField(max_length=4096, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='TaggedUserImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_time', models.DateTimeField(auto_now=True)),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='net.Tag')),
                ('tagger', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TanWCS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crval1', models.FloatField()),
                ('crval2', models.FloatField()),
                ('crpix1', models.FloatField()),
                ('crpix2', models.FloatField()),
                ('cd11', models.FloatField()),
                ('cd12', models.FloatField()),
                ('cd21', models.FloatField()),
                ('cd22', models.FloatField()),
                ('imagew', models.FloatField()),
                ('imageh', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='SourceList',
            fields=[
                ('image_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='net.Image')),
                ('source_type', models.CharField(choices=[('fits', 'FITS binary table'), ('text', 'Text list')], max_length=4)),
            ],
            bases=('net.image',),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_name', models.CharField(max_length=32)),
                ('apikey', models.CharField(max_length=16)),
                ('default_license', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='net.License')),
                ('user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publicly_visible', models.CharField(choices=[('y', 'yes'), ('n', 'no')], default='y', max_length=1)),
                ('description', models.CharField(blank=True, max_length=1024)),
                ('original_file_name', models.CharField(max_length=256)),
                ('comment_receiver', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='net.CommentReceiver')),
                ('flags', models.ManyToManyField(related_name='user_images', through='net.FlaggedUserImage', to='net.Flag')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='net.Image')),
                ('license', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='net.License')),
                ('sky_objects', models.ManyToManyField(related_name='user_images', to='net.SkyObject')),
                ('submission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_images', to='net.Submission')),
                ('tags', models.ManyToManyField(related_name='user_images', through='net.TaggedUserImage', to='net.Tag')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_images', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='taggeduserimage',
            name='user_image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='net.UserImage'),
        ),
        migrations.CreateModel(
            name='SipWCS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveSmallIntegerField(default=2)),
                ('aterms', models.TextField(default='')),
                ('bterms', models.TextField(default='')),
                ('apterms', models.TextField(default='')),
                ('bpterms', models.TextField(default='')),
                ('tan', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='net.TanWCS')),
            ],
        ),
        migrations.CreateModel(
            name='QueuedSubmission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('finished', models.BooleanField(default=False)),
                ('success', models.BooleanField(default=False)),
                ('procsub', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subs', to='net.ProcessSubmissions')),
                ('submission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='net.Submission')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='QueuedJob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('finished', models.BooleanField(default=False)),
                ('success', models.BooleanField(default=False)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='net.Job')),
                ('procsub', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='net.ProcessSubmissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='job',
            name='user_image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='net.UserImage'),
        ),
        migrations.AddField(
            model_name='flaggeduserimage',
            name='user_image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='net.UserImage'),
        ),
        migrations.CreateModel(
            name='EnhancedImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nside', models.IntegerField()),
                ('healpix', models.IntegerField()),
                ('maxweight', models.FloatField(default=0.0)),
                ('cals', models.ManyToManyField(db_table='enhancedimage_calibration', related_name='enhanced_images', to='net.Calibration')),
                ('version', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='net.EnhanceVersion')),
                ('wcs', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='net.TanWCS')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('text', models.CharField(max_length=1024)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments_left', to=settings.AUTH_USER_MODEL)),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='net.CommentReceiver')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddField(
            model_name='calibration',
            name='raw_tan',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='calibrations_raw', to='net.TanWCS'),
        ),
        migrations.AddField(
            model_name='calibration',
            name='sip',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='net.SipWCS'),
        ),
        migrations.AddField(
            model_name='calibration',
            name='sky_location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='calibrations', to='net.SkyLocation'),
        ),
        migrations.AddField(
            model_name='calibration',
            name='tweaked_tan',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='calibrations_tweaked', to='net.TanWCS'),
        ),
        migrations.CreateModel(
            name='CachedFile',
            fields=[
                ('key', models.CharField(max_length=64, primary_key=True, serialize=False, unique=True)),
                ('disk_file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='net.DiskFile')),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='comment_receiver',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='net.CommentReceiver'),
        ),
        migrations.AddField(
            model_name='album',
            name='tags',
            field=models.ManyToManyField(related_name='albums', to='net.Tag'),
        ),
        migrations.AddField(
            model_name='album',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='albums', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='album',
            name='user_images',
            field=models.ManyToManyField(related_name='albums', to='net.UserImage'),
        ),
    ]
