import tkinter as tk
import random
import time
import threading
import sys
import math


class StackingWindowGenerator:
    """极速堆叠窗口生成器 - 随机生成、可堆叠、无限制"""

    def __init__(self):
        self.root = None
        self.stop_event = threading.Event()
        self.windows = []
        self.window_count = 0
        self.start_time = 0
        self.is_running = False
        self.custom_texts = ["test", "演示", "窗口", "Python", "Hello"]
        self.screen_width = 1920
        self.screen_height = 1080
        self.cluster_centers = []

    def display_warning_dialog(self):
        """显示声明对话框"""
        dialog = tk.Tk()
        dialog.title("极速堆叠窗口生成器")
        dialog.geometry("600x500+400+250")
        dialog.resizable(False, False)
        dialog.configure(bg="#f5f6fa")
        dialog.attributes('-topmost', True)

        main_frame = tk.Frame(dialog, bg="#f5f6fa", padx=25, pady=20)
        main_frame.pack(expand=True, fill='both')

        title_label = tk.Label(
            main_frame,
            text="极速堆叠窗口生成器",
            font=("Arial", 16, "bold"),
            bg="#f5f6fa",
            fg="#2d3748",
            pady=10
        )
        title_label.pack()

        card_frame = tk.Frame(
            main_frame,
            bg="white",
            relief="solid",
            bd=1,
            padx=20,
            pady=15
        )
        card_frame.pack(fill='both', expand=True, pady=10)

        declaration_text = """程序声明：

此程序为本人与AI共同开发，遵循GPL 3.0开源协议。
采用极速堆叠算法，窗口将随机生成、可堆叠、无数量限制。
60秒自动关闭机制确保系统安全。

请在下方输入自定义文字："""

        text_label = tk.Label(
            card_frame,
            text=declaration_text,
            font=("Arial", 10),
            bg="white",
            fg="#2d3748",
            justify="left",
            wraplength=500,
            pady=10
        )
        text_label.pack(anchor='w')

        input_frame = tk.Frame(card_frame, bg="white")
        input_frame.pack(fill='x', pady=15)

        input_label = tk.Label(
            input_frame,
            text="自定义文字：",
            font=("Arial", 9),
            bg="white",
            fg="#2d3748",
            justify="left"
        )
        input_label.pack(anchor='w', pady=(0, 5))

        text_var = tk.StringVar(value="test,演示,窗口,Python,Hello")
        text_entry = tk.Entry(
            input_frame,
            textvariable=text_var,
            font=("Arial", 10),
            width=50,
            relief="solid",
            bd=1
        )
        text_entry.pack(fill='x', ipady=5, pady=5)

        hint_label = tk.Label(
            input_frame,
            text="提示：多个文字用逗号分隔，留空使用默认文字",
            font=("Arial", 8),
            bg="white",
            fg="#718096",
            pady=5
        )
        hint_label.pack(anchor='w')

        button_frame = tk.Frame(card_frame, bg="white", pady=20)
        button_frame.pack(fill='x')

        button_container = tk.Frame(button_frame, bg="white")
        button_container.pack(expand=True)

        confirmed = False
        user_texts = self.custom_texts.copy()

        def confirm_action():
            nonlocal confirmed, user_texts
            input_text = text_var.get().strip()

            if input_text:
                texts = [t.strip() for t in input_text.split(",") if t.strip()]
                user_texts = texts if texts else ["test"]
            else:
                user_texts = ["test"]

            confirmed = True
            dialog.quit()
            dialog.destroy()

        def cancel_action():
            dialog.quit()
            dialog.destroy()
            sys.exit(0)

        confirm_btn = tk.Button(
            button_container,
            text="开始极速生成",
            command=confirm_action,
            bg="#00b894",
            fg="white",
            font=("Arial", 10, "bold"),
            width=12,
            pady=8
        )
        confirm_btn.pack(side='left', padx=8)

        cancel_btn = tk.Button(
            button_container,
            text="取消退出",
            command=cancel_action,
            bg="#dfe6e9",
            font=("Arial", 10),
            width=12,
            pady=8
        )
        cancel_btn.pack(side='left', padx=8)

        footer_frame = tk.Frame(main_frame, bg="#f5f6fa", pady=10)
        footer_frame.pack(fill='x')

        footer_label = tk.Label(
            footer_frame,
            text="极速堆叠模式 - 随机生成、可堆叠、无数量限制，60秒后自动停止",
            font=("Arial", 9),
            bg="#f5f6fa",
            fg="#718096"
        )
        footer_label.pack()

        dialog.bind('<Return>', lambda e: confirm_action())
        dialog.bind('<Escape>', lambda e: cancel_action())
        text_entry.focus_set()
        text_entry.select_range(0, tk.END)

        dialog.mainloop()

        if confirmed:
            self.custom_texts = user_texts
            return True
        return False

    def get_stacking_position(self, width, height):
        """获取堆叠位置 - 完全随机，允许重叠"""
        try:
            # 完全随机位置，允许重叠
            x = random.randint(0, self.screen_width - width)
            y = random.randint(0, self.screen_height - height)

            return x, y

        except:
            return random.randint(0, 800), random.randint(0, 600)

    def create_stacking_window(self, window_id):
        """创建堆叠窗口"""
        try:
            window = tk.Toplevel()
            window.title(f"窗口 {window_id}")

            # 随机窗口尺寸
            width = random.randint(200, 400)
            height = random.randint(60, 120)

            # 获取随机位置
            x, y = self.get_stacking_position(width, height)
            window.geometry(f"{width}x{height}+{x}+{y}")
            window.resizable(False, False)

            # 生成随机颜色
            bg_color = self._generate_color()
            fg_color = self._get_contrast_color(bg_color)

            window.configure(bg=bg_color)
            window.attributes('-topmost', True)

            # 随机透明度
            if random.random() < 0.3:  # 30%的窗口有透明度
                alpha = random.uniform(0.7, 0.9)
                window.attributes('-alpha', alpha)

            # 内容区域
            text = random.choice(self.custom_texts)
            label = tk.Label(
                window,
                text=text,
                font=("Arial", random.randint(8, 12)),
                bg=bg_color,
                fg=fg_color,
                wraplength=width - 20,
                justify="center",
                padx=10,
                pady=8
            )
            label.pack(expand=True)

            return window

        except Exception as e:
            return None

    def _generate_color(self):
        """生成随机颜色"""
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return f"#{r:02x}{g:02x}{b:02x}"

    def _get_contrast_color(self, bg_color):
        """获取对比色"""
        try:
            r = int(bg_color[1:3], 16)
            g = int(bg_color[3:5], 16)
            b = int(bg_color[5:7], 16)
            brightness = (r * 299 + g * 587 + b * 114) / 1000
            return "#000000" if brightness > 128 else "#ffffff"
        except:
            return "#000000"

    def start_generation(self):
        """开始生成窗口"""
        if not self.display_warning_dialog():
            return

        self.root = tk.Tk()
        self.root.withdraw()
        self.is_running = True
        self.start_time = time.time()

        print("极速堆叠窗口生成器启动")
        print(f"自定义文字: {', '.join(self.custom_texts)}")
        print("模式: 随机生成、可堆叠、无数量限制")
        print("窗口生成中... 60秒后自动结束")

        gen_thread = threading.Thread(target=self._ultra_fast_generation, daemon=True)
        gen_thread.start()

        stop_thread = threading.Thread(target=self._auto_stop, daemon=True)
        stop_thread.start()

        monitor_thread = threading.Thread(target=self._monitor, daemon=True)
        monitor_thread.start()

        try:
            self.root.mainloop()
        except KeyboardInterrupt:
            self.stop_program()

    def _ultra_fast_generation(self):
        """极速生成循环"""
        last_status_time = time.time()
        batch_sizes = [1, 2, 3, 5]  # 随机批量大小

        while self.is_running and not self.stop_event.is_set():
            try:
                # 极速生成 - 极短延迟
                time.sleep(0.01)  # 0.01秒延迟，极速生成

                # 随机批量创建窗口
                batch_size = random.choice(batch_sizes)
                for _ in range(batch_size):
                    # 无数量限制，持续生成
                    window = self.create_stacking_window(self.window_count + 1)
                    if window:
                        self.windows.append(window)
                        self.window_count += 1

                # 状态输出
                current_time = time.time()
                if current_time - last_status_time > 1:
                    elapsed = current_time - self.start_time
                    remaining = max(0, 60 - elapsed)
                    active = len([w for w in self.windows if w.winfo_exists()])
                    speed = self.window_count / elapsed if elapsed > 0 else 0
                    print(
                        f"速度: {speed:.1f}窗口/秒, 生成: {self.window_count}, 活动: {active}, 剩余: {remaining:.0f}秒")
                    last_status_time = current_time

            except Exception as e:
                time.sleep(0.1)

    def _auto_stop(self):
        """自动停止"""
        time.sleep(60)
        if self.is_running:
            print("60秒时间到，自动停止")
            self.stop_program()

    def _monitor(self):
        """监控"""
        while self.is_running and not self.stop_event.is_set():
            try:
                # 清理已关闭窗口
                self.windows = [w for w in self.windows if w.winfo_exists()]
                time.sleep(2)
            except:
                time.sleep(2)

    def stop_program(self):
        """停止程序"""
        if not self.is_running:
            return

        self.is_running = False
        self.stop_event.set()

        print("正在关闭程序...")

        close_count = 0
        for window in self.windows:
            try:
                if window.winfo_exists():
                    window.destroy()
                    close_count += 1
            except:
                pass

        try:
            self.root.quit()
            self.root.destroy()
        except:
            pass

        run_time = time.time() - self.start_time
        windows_per_second = self.window_count / run_time if run_time > 0 else 0

        print("程序运行结束")
        print(f"运行时间: {run_time:.1f}秒")
        print(f"生成窗口: {self.window_count}个")
        print(f"关闭窗口: {close_count}个")
        print(f"平均速度: {windows_per_second:.1f} 窗口/秒")


def main():
    """主函数"""
    generator = StackingWindowGenerator()

    try:
        import signal
        def signal_handler(sig, frame):
            generator.stop_program()

        signal.signal(signal.SIGINT, signal_handler)
    except:
        pass

    try:
        generator.start_generation()
    except Exception as e:
        print(f"程序错误: {e}")
    finally:
        generator.stop_program()


if __name__ == "__main__":
    main()
