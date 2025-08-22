#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
My-Neuro 功能检查脚本
检查所有新功能模块是否可用
"""

import sys
import importlib

def check_module(module_name, feature_name, required=True):
    """检查模块是否可用"""
    try:
        importlib.import_module(module_name)
        print(f"✅ {feature_name}: 可用")
        return True
    except ImportError as e:
        status = "❌" if required else "⚠️"
        print(f"{status} {feature_name}: 不可用 ({e})")
        return False

def main():
    print("🔍 My-Neuro 功能检查")
    print("=" * 50)
    
    # 基础依赖检查
    print("📦 基础依赖:")
    basic_modules = [
        ("PyQt5", "PyQt5界面库", True),
        ("openai", "OpenAI API库", True), 
        ("keyboard", "键盘控制库", True),
        ("pygame", "音频播放库", True),
    ]
    
    basic_available = 0
    for module, name, required in basic_modules:
        if check_module(module, name, required):
            basic_available += 1
    
    print(f"\n基础依赖: {basic_available}/{len(basic_modules)}")
    
    # 新功能依赖检查
    print("\n🆕 新功能依赖:")
    new_modules = [
        ("flask", "Web界面支持", False),
        ("flask_socketio", "实时通信支持", False),
        ("sqlite3", "数据库支持", True),
        ("pandas", "数据处理支持", False),
        ("jieba", "中文分词支持", False),
    ]
    
    new_available = 0
    for module, name, required in new_modules:
        if check_module(module, name, required):
            new_available += 1
    
    print(f"\n新功能依赖: {new_available}/{len(new_modules)}")
    
    # 功能模块检查
    print("\n🧩 功能模块:")
    feature_modules = [
        ("memory_mod.long_term_memory", "长期记忆系统"),
        ("real_emotion_mod.real_emotion_system", "真实情感系统"),
        ("teaching_mod.ai_teaching_system", "AI讲课系统"),
        ("game_mod.game_companion", "游戏陪玩系统"),
        ("web_interface.web_server", "Web界面系统"),
    ]
    
    features_available = 0
    for module, name in feature_modules:
        if check_module(module, name, False):
            features_available += 1
    
    print(f"\n功能模块: {features_available}/{len(feature_modules)}")
    
    # 总体评估
    print("\n" + "=" * 50)
    total_available = basic_available + new_available + features_available
    total_modules = len(basic_modules) + len(new_modules) + len(feature_modules)
    
    if total_available == total_modules:
        print("🎉 所有功能完全可用！")
        print("💡 建议: 运行 'python main_chat.py' 启动完整版")
    elif basic_available == len(basic_modules):
        print("✅ 基础功能可用，部分新功能可能不可用")
        print("💡 建议: 安装缺失依赖或运行基础版本")
    else:
        print("❌ 存在关键依赖缺失")
        print("💡 建议: 先安装基础依赖包")
    
    print(f"\n📊 总体可用率: {total_available}/{total_modules} ({total_available/total_modules*100:.1f}%)")
    
    # 安装建议
    if new_available < len(new_modules):
        print("\n📝 安装缺失的新功能依赖:")
        print("pip install Flask Flask-SocketIO pandas jieba")
    
    return total_available == total_modules

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)