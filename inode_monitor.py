def check_inode_usage(total_inodes, used_inodes):
    usage = (used_inodes / total_inodes) * 100

    print(f"Total Inodes : {total_inodes}")
    print(f"Used Inodes  : {used_inodes}")
    print(f"Inode Usage  : {usage:.2f}%")

    if usage >= 90:
        print("🚨 ALERT: Inode usage is critically high!")
    elif usage >= 80:
        print("⚠️ WARNING: Inode usage is high!")
    else:
        print("✅ Inode usage is healthy.")


# Simulated inode data
check_inode_usage(10_000_000, 9_200_000)